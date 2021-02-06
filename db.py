import sqlite3


def data():

    database_name = 'db.sqlite3'
    connection = sqlite3.connect(database_name)
    cur = connection.cursor()

    drop_table = "DROP TABLE IF EXISTS Todo;"
    create_table = '''CREATE TABLE Todo (Id INTEGER PRIMARY KEY,
                Task varchar(100) NOT NULL,
                Description varchar(2048) NOT NULL);'''

    insert_task1 = '''INSERT INTO Todo (Task, Description) VALUES
                ('Take the first 2 courses of Python 4 Everybody by Charles
                    Severance for a good intro to Python',
                'This is the first description');'''
    insert_task2 = '''INSERT INTO Todo (Task, Description) VALUES
                ('Visit the Python website and read some docs',
                'This is the second description'); '''
    insert_task3 = '''INSERT INTO Todo (Task, Description) VALUES
                ('VS Code is the best editor',
                    'This is the third description');'''        
    insert_task4 = '''INSERT INTO Todo (Task, Description) VALUES
                ('Choose your favourite WSGI-Framework',
                    'This is the fourth description');'''

    cur.executescript(f'{drop_table} {create_table} {insert_task1} {insert_task2} {insert_task3} {insert_task4}')
    connection.commit()
    cur.close()
