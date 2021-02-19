import sqlite3
from bottle import route, run, template,\
    static_file, error, request
from db import SeedData


def database_connection():
    connection = sqlite3.connect(SeedData.database_name)
    cur = connection.cursor()
    return cur, connection


@route('/')  # main route
def home():
    cur, connection = database_connection()
    cur.execute("SELECT Id, Task, Description FROM Todo;")
    result = cur.fetchall()
    cur.close()

    return template('templates/table', rows=result)


def get_request(form_value):
    return request.GET.get(form_value, '').strip()


@route('/new', method='GET')
def new_item():
    if get_request('save'):
        new = get_request('task')
        description = get_request('description')

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

    if get_request('save'):
        edit = get_request('task')
        description = get_request('description')

        cur, connection = database_connection()
        cur.execute('UPDATE Todo SET Task = ?, Description = ? WHERE Id = ?',
                    (edit, description, number))
        connection.commit()
        cur.close()

        return '''
                <p> The item %s was sucessfully edited</p>
                <p>Go <a href="/"> Home</a></p>''' % str(number)

    elif get_request('delete'):
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
    if len(cur_data) < 2:
        return '<h3>Task not found </h3>'
    else:
        task_data = cur_data[0]
        description_data = cur_data[1]

    return template('templates/edit_task', old_task=task_data,
                    description=description_data, number=number)


@route('/help')
def help():
    return static_file('templates/help.html', root='.')


@error(403)
def error_403(code):
    return template('templates/403_error')


@error(404)
def error_404(code):
    return template('templates/404_error')


if __name__ == "__main__":
    data = SeedData()
    data.connect_data()
    run(debug=True, reloader=True)
