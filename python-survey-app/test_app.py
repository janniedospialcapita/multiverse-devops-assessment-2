import pytest
import os
import sys
import sqlite3

sys.path.append('./app')

from input import *
from sqldb import *
from output import read_output

from app import main

os.chdir("./app/")


def test_input_is_list_of_lists():
    
    # Arrange
    filename = "results.csv"
    expected_output = list

    # Act
    output = type(get_input(filename))
    output2 = type(get_input(filename)[0])

    # Assert
    assert output == expected_output
    assert output2 == expected_output

def test_columns():

    # Arrange
    filename = "results.csv"

    expected_cols = [
        'user_id', 
        'first_name', 
        'last_name', 
        'answer_1', 
        'answer_2', 
        'answer_3',
        ]
    
    # Act
    input_data = get_input(filename)

    # Assert
    assert input_data[0] == expected_cols


def test_duplicates_removal():

    # Arrange
    filename = "results.csv"
    input_data = get_input(filename)

    input_data2 = [
        ['cheese', 'wine'], 
        ['cheese', 'kale'], 
        ['spinach', 'tea'], 
        ['cheese', 'wine'], 
        ['spinach', 'coffee']
        ]

    distinct_list = []
    dupe_list = []

    # Act
    input_data = remove_duplicates(input_data)
    input_data2 = remove_duplicates(input_data2)

    for x in [input_data, input_data2]:
        for i in x:
            if i not in distinct_list:
                distinct_list.append(i)
            else:
                dupe_list.append(i)

    # Assert
    assert len(dupe_list) == 0
    

def test_remove_empty_lines():

    # Arrange
    filename = "results.csv"
    input_data = get_input(filename)
    empty_row = ['' for x in range(len(input_data[0]))]
    input_data.append(empty_row)

    # Act
    output = remove_empty_lines(input_data)

    # Assert
    assert empty_row not in output

def test_capitalise():

    # Arrange
    filename = "results.csv"
    input_data = get_input(filename)
    input_data = remove_empty_lines(input_data)
    lower_case_row = ['3', 'test', 'mctest', 't', 't', 0]
    input_data.append(lower_case_row)
    first_name = []
    last_name = []

    # Act
    input_data = capitalise_names(input_data)
    
    for i in input_data[1:]:
        first_name.append(i[1])
        last_name.append(i[2])

    first_name_upper = [x for x in first_name if x[0].isupper()]
    last_name_upper = [x for x in last_name if x[0].isupper()]

    # Assert
    assert first_name_upper == first_name
    assert last_name_upper == last_name
    assert 'McTest' in last_name_upper



def test_answer3_validation():
    
    # Arrange
    filename = "results.csv"
    input_data = get_input(filename)
    input_data = remove_empty_lines(input_data)
    input_data = capitalise_names(input_data)
    invalid_rows = [
        ['', '', '', '', '', 15],
        ['', '', '', '', '',0],
    ]
    input_data.extend(invalid_rows)
    # Act
    input_data = validate_answer3(input_data)

    answer_3 = []

    for i in input_data[1:]:
        answer_3.append(int(i[5]))

    fail = [x for x in answer_3 if x > 10 or x < 1]

    # Assert
    assert len(fail) == 0


def test_save_file(tmp_path):

    # Arrange
    directory = tmp_path / "sub"
    directory.mkdir()
    result_filename = 'clean_results.csv'
    temp_file_dir = directory.joinpath(result_filename)
    filename = 'results.csv'    

    # Act
    input_data = get_input(filename)
    save_output(input_data, temp_file_dir)

    # Assert
    output = get_input(temp_file_dir)
    expected_output = input_data
    assert output  == expected_output

def test_read_output():

    # Arrange
    expected_output = list
    test_data = 'results.csv'

    # Act
    output_data = read_output(test_data)
    output = type(output_data)

    # Assert
    assert output == expected_output

def test_main_sqlite():

    # Arrange:
    test_data = [
    [1, 'Test', 'Test', 'yes', 'c', 7],
    [2, 'Test', 'Test', 'yes', 'b', 7],
    ]
    
    # Act
    main(data=test_data)
    db = sqlite3.connect('results.db')
    test_result = select_all(db, 'clean_results')
    test_result = [list(x) for x in test_result]
  
    # Assert
    assert len([x for x in test_data if x in test_result]) == 2

    # Cleanup
    db = sqlite3.connect('results.db')
    for table in ['results', 'clean_results']:
        delete_from_table(db, table, 'last_name', 'Test')
    db.close()
