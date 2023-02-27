import pandas as pd
import numpy as np
import re
from extract import get_input
from extract import remove_duplicates
from extract import remove_empty_lines
from extract import capitalise_names
from extract import validate_answer3

def test_input_is_list():
    
    # Arrange
    filename = "results.csv"
    expected_output = list

    # Act
    output = get_input(filename)

    # Assert
    assert type(output) == expected_output

def test_duplicates_removal():
    
    # Arrange
    filename = "results.csv"
    df = pd.read_csv(filename)
    df = df.drop_duplicates()
    expected_output = df.shape[0] + 1
    
    # Act
    input = get_input(filename)
    output = remove_duplicates(input)
    
    # Assert
    assert len(output) == expected_output

def test_empty_line_removal():
    
    # Arrange
    filename = "results.csv"
    df = pd.read_csv(filename)
    df = df.dropna(how='all')
    expected_output = df.shape[0] + 1

     # Act
    input = get_input(filename)
    output = remove_empty_lines(input)
    
    # Assert
    assert len(output) == expected_output

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
    
    # Arange
    filename = "results.csv"
    df = pd.read_csv(filename)
    df = df.dropna(how='all')
    df = df[(df['answer_3'] > 0) & (df['answer_3'] < 11)]
    expected_output = len(df) + 1
    
    # Act
    input = get_input(filename)
    input = remove_empty_lines(input)
    output = validate_answer3(input)

    # Assert
    assert len(output) == expected_output

def test_input_fails_if_file_not_found():
    pass