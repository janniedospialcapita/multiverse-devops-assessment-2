from input import get_input
from input import remove_duplicates
from input import remove_empty_lines
from input import capitalise_names
from input import validate_answer3
from input import save_output
from output import read_output

filename = "results.csv"

data = get_input(filename)
data = remove_duplicates(data)
data = remove_duplicates(data)
data = remove_empty_lines(data)
data = capitalise_names(data)
data = validate_answer3(data)
save_output(data, 'clean_results.csv')
read_output()
