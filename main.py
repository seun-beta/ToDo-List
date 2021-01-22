import sqlite3
# Importing all the needed bottle modules 
from bottle import route, run, debug, template, request , static_file, error 
import db

db.data()
database_name = 'db.sqlite'

def database_connection():
    connection = sqlite3.connect(database_name)
    return connection.cursor()

def commit_data():
    connection = sqlite3.connect(database_name)
    
    return connection


# main route
@route('/')  
def home():
    cur = database_connection()
    cur.execute("SELECT Id, Task, Description FROM Todo;")
    result = cur.fetchall() # Returns a list of tuple from the database
    cur.close()
    output = template('templates/table', rows=result)
    return output

@route('/new', method = 'GET')
def new_item():
    if request.GET.get('save','').strip():

        new = request.GET.get('task', '').strip()
        description = request.GET.get('description','').strip()

        cur = database_connection()

        cur.execute("INSERT INTO Todo (Task,Description) VALUES (?,?)", (new,description))
        new_id = cur.lastrowid
        
        connection = commit_data()
        connection.commit()
        cur.close()

        return template('templates/success', new_id = new_id)
    else:
        return template('templates/new_task')


@route('/edit/:number' ,method = 'GET' )
def edit_item(number):

    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        description = request.GET.get('description','').strip()
        cur = database_connection()
        cur.execute('UPDATE Todo SET Task = ?, Description = ? WHERE Id = ?',(edit, description, number))
        connection = commit_data()
        connection.commit()

        return '<p> The item %s was sucessfully edited</p><p>Go <a href="/"> Home</a></p>' %str(number)

    elif request.GET.get('delete','').strip():
        cur = database_connection()
        cur.execute('DELETE FROM Todo WHERE Id = ?',(number,))
        connection = commit_data()
        connection.commit()

        return '<p> The item %s was sucessfully deleted</p><p><a href="/">Go Home</a></p>' %str(number)

    else:
        cur = database_connection()
        cur.execute('SELECT Task, Description FROM Todo WHERE Id = ?', (str(number),))
        cur_data = cur.fetchone()
        print (cur_data)
        for i in cur_data:
            task_data = cur_data[0]
            description_data = cur_data[1]

        return template('templates/edit_task',old_task = task_data, description = description_data  ,number=number)    

@route('/help') # The custome help page that provides information about the developer
def help():
    return static_file ('templates/help.html', root='.')
    
@error(403)
def mistake403 (code):
    return template('templates/403_error')

@error(404)           #This block of code handles 404 (not found errors)
def mistake404 (code):
    return template('templates/404_error')


if __name__ == "__main__":
    run(debug=True, reloader=True)