import sqlite3


class SeedData:

    database_name = 'db.sqlite3'
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

    def connect_data(self):
        
        connection = sqlite3.connect(SeedData.database_name)
        cur = connection.cursor()
        cur.executescript(f'''{SeedData.drop_table} {SeedData.create_table} {SeedData.insert_task1}
                                {SeedData.insert_task2} {SeedData.insert_task3} {SeedData.insert_task4}''')
        connection.commit()
        cur.close()
        return cur, connection
