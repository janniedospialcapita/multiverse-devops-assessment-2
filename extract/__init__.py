import csv

def get_input(filename):
    

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data


def remove_duplicates(data):
    data_deduped =[]
    for x in data:
        if x not in data_deduped:
            data_deduped.append(x)

    return data_deduped