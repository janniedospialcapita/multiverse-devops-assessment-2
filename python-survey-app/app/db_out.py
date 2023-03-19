import sqlite3
import sys
from output import read_output
from sqldb import select_all
    

def db_out():
    
    db = sqlite3.connect('results.db')
    clean_results = select_all(db, 'clean_results')
    data = read_output(data=clean_results)

    if __name__ != '__main__': 
        return data

if __name__ == '__main__': 
    sys.exit(db_out())