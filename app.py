import pandas as pd
from extract import get_input
from extract import remove_duplicates
from extract import remove_empty_lines
from extract import capitalise_names
from extract import validate_answer3
from extract import save_output

filename = "results.csv"

data = get_input(filename)
data = remove_duplicates(data)
data = remove_duplicates(data)
data = remove_empty_lines(data)
data = capitalise_names(data)
data = validate_answer3(data)
save_output(data, 'clean_results.csv')

for i in data:
    print(i)