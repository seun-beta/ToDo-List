import sqlite3
# Importing all the needed bottle modules
from bottle import route, run, template,\
    static_file, error, request
import db
db.SeedData


database_name = db.SeedData.database_name


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


    return template('templates/table', rows=result)

# Helper function  
def request_func(get_request):
    result = request.GET.get(get_request, '').strip()
    return result

@route('/new', method='GET')
def new_item():
    if request_func('save'):

        new = request_func('task')
        
        description = request_func('description')

        cur, connection = database_connection()
        cur.execute("INSERT INTO Todo (Task,Description) VALUES (?,?)",
                    (new, description,))
        new_id = cur.lastrowid
        connection.commit()
        cur.close()
        return template('templates/success', new_id=str(new_id))

    return template('templates/new_task')


@route('/edit/:number', method='GET')
def edit_item(number):

    if request_func('save'):
        edit = request_func('task')
        description = request_func('description')
        cur, connection = database_connection()
        cur.execute('UPDATE Todo SET Task = ?, Description = ? WHERE Id = ?',
                    (edit, description, number))
        connection.commit()
        cur.close()

        return '''
                <p> The item %s was sucessfully edited</p>
                <p>Go <a href="/"> Home</a></p>''' % str(number)

    elif request_func('delete'):
        cur, connection = database_connection()
        cur.execute('DELETE FROM Todo WHERE Id = ?', (number,))
        connection.commit()

        return '''
        <p> The item %s was sucessfully deleted</p>
        <p><a href="/">Go Home</a></p>''' % str(number)

    
    cur, connection = database_connection()
    cur.execute('SELECT Task, Description FROM Todo WHERE Id = ?',
                (str(number),))
    cur_data = cur.fetchone()
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
