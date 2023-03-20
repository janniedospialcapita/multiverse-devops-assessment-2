import sqlite3 
import sys

from input import get_input
from input import remove_duplicates
from input import remove_empty_lines
from input import capitalise_names
from input import validate_answer3
from input import save_output

from sqldb import * 

filename = "results.csv"

def main(filename=None, data=None): 
    db = sqlite3.connect('results.db')

    if data is None:
        data = get_input(filename)

    create_table_results(db)
    show_tables(db)
    describe_table(db, 'results')
    select_all(db, 'results')
    insert_data(db, 'results', data)

    data = select_all(db, 'results')
    data = [list(x) for x in data]
    data = remove_duplicates(data)
    data = remove_duplicates(data)
    data = remove_empty_lines(data)
    data = capitalise_names(data)
    data = validate_answer3(data)
    save_output(data, 'clean_results.csv')

    create_table_clean_results(db)
    show_tables(db)
    describe_table(db, 'clean_results')
    insert_data(db, 'clean_results', data)
    db.close()
    
    print()
    print('Results cleaned, saved and added to database')

if __name__ == '__main__': 
    sys.exit(main(filename=filename))