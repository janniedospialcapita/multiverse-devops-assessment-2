import sys
from output import read_output
    
filename = 'clean_results.csv'

def app_out(filename=None):

    data = read_output(filename)

    if __name__ != '__main__': 
        return data

if __name__ == '__main__': 
    sys.exit(app_out(filename=filename))
