import sqlite3

def data():
    database_name = 'db.sqlite'
    connection = sqlite3.connect(database_name)
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS Todo")
    cur.execute("CREATE TABLE Todo (Id INTEGER PRIMARY KEY, Task varchar(100) NOT NULL, Description varchar(2048) NOT NULL); ")
    cur.execute("INSERT INTO Todo (Task, Description) VALUES ('Take the first 2 courses of Python 4 Everybody by Charles Severance for a good intro to Python','This is the first description')")
    cur.execute("INSERT INTO Todo (Task, Description) VALUES ('Visit the Python website and read some docs','This is the second description') ")
    cur.execute("INSERT INTO Todo (Task, Description) VALUES ('VS Code is the best editor', 'This is the third description')")
    cur.execute("INSERT INTO Todo (Task, Description) VALUES ('Choose your favourite WSGI-Framework', 'This is the fourth description')")
    connection.commit()
    cur.close()