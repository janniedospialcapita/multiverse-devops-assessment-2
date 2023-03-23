import sqlite3
from sqlite3 import OperationalError

def create_table_results(db): 
    db.execute(
        '''
        CREATE TABLE IF NOT EXISTS results(
                user_id INTEGER NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                answer_1 TEXT NOT NULL,
                answer_2 TEXT NOT NULL,
                answer_3 INTEGER NOT NULL,
                PRIMARY KEY (user_id, first_name, last_name, answer_1, answer_2, answer_3)
                )
                '''
    )

def show_tables(db):
    try:
        cursor = db.execute(
            ''' 
            SELECT name 
            FROM sqlite_schema 
            WHERE type ='table' AND name NOT LIKE 'sqlite_%' 
            ''')
    except OperationalError:
        cursor = db.execute(
            ''' 
            SELECT name 
            FROM sqlite_master 
            WHERE type ='table' AND name NOT LIKE 'sqlite_%' 
            ''')
    result = cursor.fetchall() 
    print(f'Tables in the database: {result}') 
    
def describe_table(db, table):
    try: 
        cursor = db.execute(
            f'SELECT sql FROM sqlite_schema WHERE name = "{table}"'
            )
    except OperationalError:
        cursor = db.execute(
            f'SELECT sql FROM sqlite_master WHERE name = "{table}"'
            )
    result = cursor.fetchone() 
    print(result[0])

def select_all(db, table):
    headers = db.execute(f"PRAGMA table_info({table});")
    headers = headers.fetchall()
    headers = [x[1] for x in headers]
    cursor = db.execute(f'SELECT * FROM {table}')
    result = cursor.fetchall()
    result.insert(0, headers)
    return result

def insert_data(db, table, data):
    db.executemany(f'INSERT OR IGNORE INTO {table} VALUES (?, ?, ?, ?, ?, ?)', data)
    db.commit()

def create_table_clean_results(db):
    db.execute(
        '''
        CREATE TABLE IF NOT EXISTS clean_results(
        user_id INTEGER NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        answer_1 TEXT NOT NULL,
        answer_2 TEXT NOT NULL,
        answer_3 INTEGER NOT NULL,
        PRIMARY KEY (user_id, first_name, last_name, answer_1, answer_2, answer_3)
        )
        '''
    )

def delete_from_table(db, table, column, value):
    cursor = db.execute(f'DELETE FROM {table} WHERE {column} = ?', (value,))
    db.commit()