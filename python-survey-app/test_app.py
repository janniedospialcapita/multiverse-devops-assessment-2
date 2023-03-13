import pytest
import pandas as pd
import numpy as np
import re

from input import get_input
from input import remove_duplicates
from input import remove_empty_lines
from input import capitalise_names
from input import validate_answer3
from input import save_output
from output import read_output

def test_input_is_list():
    
    # Arrange
    filename = "results.csv"
    expected_output = list

    # Act
    output = type(get_input(filename))

    # Assert
    assert output == expected_output

def test_duplicates_removal():
    
    # Arrange
    filename = "results.csv"
    df = pd.read_csv(filename)
    df = df.drop_duplicates()
    expected_output = df.shape[0] + 1
    
    # Act
    input = get_input(filename)
    output = len(remove_duplicates(input))
    
    # Assert
    assert output == expected_output

def test_empty_line_removal():
    
    # Arrange
    filename = "results.csv"
    df = pd.read_csv(filename)
    df = df.dropna(how='all')
    expected_output = df.shape[0] + 1

     # Act
    input = get_input(filename)
    output = len(remove_empty_lines(input))
    
    # Assert
    assert output == expected_output

def test_capitalise():
    
    # Arrange
    filename = "results.csv"
    def McOcase(match):
        return match.group(1)+match.group(2).upper()
    df = pd.read_csv(filename)
    df = df.replace(np.NaN, '')
    df['first_name'] = df['first_name'].str.capitalize()
    df['last_name'] = df['last_name'].str.capitalize()
    df['last_name']=df.last_name.str.replace(r"\b(Mc)([a-z])", McOcase,  regex=True, flags=re.IGNORECASE)
    df['last_name']=df.last_name.str.replace(r"(\bO\')([a-z])", McOcase,  regex=True, flags=re.IGNORECASE)
    df['last_name']=df.last_name.str.replace(r"(\')([a-z])", McOcase,  regex=True, flags=re.IGNORECASE)
    expected_output1 = df['first_name'].to_list()
    expected_output2 = df['last_name'].to_list()

    # Act
    input = get_input(filename)
    output = capitalise_names(input)
    output1 = [x[1] for x in input[1:]]
    output2 = [x[2] for x in input[1:]] 

    # Assert
    assert output1 == expected_output1
    assert output2 == expected_output2

def test_answer3_validation():
    
    # Arrange
    filename = "results.csv"
    df = pd.read_csv(filename)
    df = df.dropna(how='all')
    df = df[(df['answer_3'] > 0) & (df['answer_3'] < 11)]
    expected_output = len(df) + 1
    
    # Act
    input = get_input(filename)
    input = remove_empty_lines(input)
    output = len(validate_answer3(input))

    # Assert
    assert output == expected_output


def test_save_file(tmp_path):

    # Arrange
    directory = tmp_path / "sub"
    directory.mkdir()
    result_filename = 'clean_results.csv'
    temp_file_dir = directory.joinpath(result_filename)
    filename = 'results.csv'    

    # Act
    input = get_input(filename)
    save_output(input, temp_file_dir)

    # Assert
    output = get_input(temp_file_dir)
    expected_output = input
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

