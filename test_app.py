import pandas as pd
import numpy as np
import re
from extract import get_input
from extract import remove_duplicates
from extract import remove_empty_lines
from extract import capitalise_names

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
    
    # Act
    input = get_input(filename)
    output = remove_duplicates(input)

    expected_output = df.shape[0] + 1

    # Assert
    assert len(output) == expected_output

def test_empty_line_removal():
    # Arrange
    filename = "results.csv"
    df = pd.read_csv(filename)
    df = df.dropna(how='all')

     # Act
    input = get_input(filename)
    output = remove_empty_lines(input)

    expected_output = df.shape[0] + 1

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

    # Act
    input = get_input(filename)
    output = capitalise_names(input)
    output1 = [x[1] for x in input[1:]]
    output2 = [x[2] for x in input[1:]] 

    expected_output1 = df['first_name'].to_list()
    expected_output2 = df['last_name'].to_list()

    # Assert
    assert output1 == expected_output1
    assert output2 == expected_output2


def test_input_fails_if_file_not_found():
    pass