import sqlite3 
import sys

from input import *
from sqldb import * 

filename = "./data/in/results.csv"

def main(filename=None, data=None): 
    print(f'sqlite3 version: {sqlite3.sqlite_version}')
    print()

    db = sqlite3.connect('./db/results.db')

    if data is None:
        data = get_input(filename)

    create_table_results(db)
    describe_table(db, 'results')
    select_all(db, 'results')
    if data[0][0] == 'user_id':
        data_to_load = data[1:]
    else:
        data_to_load = data
    insert_data(db, 'results', data_to_load)

    data = [list(x) for x in data]
    data = remove_duplicates(data)
    data = remove_empty_lines(data)
    data = capitalise_names(data)
    data = validate_answer3(data)
    save_output(data, './data/out/clean_results.csv')

    create_table_clean_results(db)
    describe_table(db, 'clean_results')
    print()
    show_tables(db)
    if data[0][0] == 'user_id':
        data_to_load = data[1:]
    else:
        data_to_load = data
    insert_data(db, 'clean_results', data_to_load)
    db.close()
    
    print()
    print('Results cleaned, saved and added to the database')

if __name__ == '__main__': 
    sys.exit(main(filename=filename))