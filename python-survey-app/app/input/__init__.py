import csv
import re

def get_input(filename):
    

    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)

    return data


def remove_duplicates(data):
    data_deduped = []
    for i in data:
        if i not in data_deduped:
            data_deduped.append(i)

    return data_deduped


def remove_empty_lines(data):
    lines_not_empty = []
    for i in data:
        if len([x for x in i if x != '']) > 0:
            lines_not_empty.append(i)

    return lines_not_empty


def capitalise_names(data):
    def McOcase(match):
        return match.group(1)+match.group(2).upper()

    for i in data[1:]:
        i[1] = i[1].capitalize()
        i[2] = i[2].capitalize()
        i[2] = re.sub(r"(\bMc)([a-z])", McOcase, i[2])
        i[2] = re.sub(r"(\bO\')([a-z])", McOcase, i[2])
        i[2] = re.sub(r"(\')([a-z])", McOcase, i[2])

    return data

def validate_answer3(data):
    validated_answer3 = [x for x in data[1:] if int(x[5]) > 0 and int(x[5])<11]
    validated_answer3.insert(0, data[0])
    return validated_answer3


def save_output(data, file_path):
    
    with open(file_path, 'w') as filename:
        writer = csv.writer(filename)
        writer.writerows(data)