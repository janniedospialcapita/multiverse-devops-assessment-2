import csv

def get_input(filename):
    

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data


def remove_duplicates(data):
    data_deduped =[]
    for i in data:
        if i not in data_deduped:
            data_deduped.append(i)

    return data_deduped


def remove_empty_lines(data):
    lines_not_empty =[]
    for i in data:
        if len([x for x in i if x != '']) > 0:
            lines_not_empty.append(i)

    return lines_not_empty