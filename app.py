import pandas as pd
from extract import get_input
from extract import remove_duplicates
from extract import remove_empty_lines
from extract import capitalise_names

filename = "results.csv"

data = get_input(filename)
data = remove_duplicates(data)
data = remove_duplicates(data)
data = remove_empty_lines(data)
data = capitalise_names(data)

for i in data:
    print(i)