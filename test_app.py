import pandas as pd
from extract import get_input
from extract import remove_duplicates
from extract import remove_empty_lines

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

def test_input_fails_if_file_not_found():
    pass