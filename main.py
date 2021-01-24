import sqlite3
# Importing all the needed bottle modules
from bottle import route, run, template, static_file, error, request
import db

db.data()
database_name = 'db.sqlite3'


def database_connection():
    connection = sqlite3.connect(database_name)
    cur = connection.cursor()
    return cur, connection


# main route
@route('/')
def home():
    cur, connection = database_connection()
    cur.execute("SELECT Id, Task, Description FROM Todo;")
    result = cur.fetchall()   # Returns a list of tuple from the database
    cur.close()
    output = template('templates/table', rows=result)
    return output


@route('/new', method='GET')
def new_item():
    if request.GET.get('save', '').strip():

        new = request.GET.get('task', '').strip()
        description = request.GET.get('description', '').strip()

        cur, connection = database_connection()
        cur.execute("INSERT INTO Todo (Task,Description) VALUES (?,?)",
                    (new, description,))
        new_id = cur.lastrowid()
        
        
        connection.commit()
        cur.close()

        return template('templates/success', new_id=str(new_id))
    else:
        return template('templates/new_task')


@route('/edit/:number', method='GET')
def edit_item(number):

    if request.GET.get('save', '').strip():
        edit = request.GET.get('task', '').strip()
        description = request.GET.get('description', '').strip()
        cur, connection = database_connection()
        
        cur.execute('UPDATE Todo SET Task = ?, Description = ? WHERE Id = ?',
                    (edit, description, number))
        
        connection.commit()
        cur.close()
        
        return '''
                <p> The item %s was sucessfully edited</p>
                <p>Go <a href="/"> Home</a></p>''' % str(number)

    elif request.GET.get('delete', '').strip():
        cur, connection = database_connection()
        cur.execute('DELETE FROM Todo WHERE Id = ?', (number,))
        connection.commit()

        return '''
        <p> The item %s was sucessfully deleted</p>
        <p><a href="/">Go Home</a></p>''' % str(number)

    else:
        cur, connection = database_connection()
        cur.execute('SELECT Task, Description FROM Todo WHERE Id = ?',
                    (str(number),))
        cur_data = cur.fetchone()
        print(cur_data)
        for i in cur_data:
            task_data = cur_data[0]
            description_data = cur_data[1]

        return template('templates/edit_task', old_task=task_data,
                        description=description_data, number=number)


@route('/help')
def help():
    return static_file('templates/help.html', root='.')


@error(403)
def mistake403(code):
    return template('templates/403_error')


@error(404)
def mistake_404(code):
    return template('templates/404_error')


if __name__ == "__main__":
    run(debug=True, reloader=True)
