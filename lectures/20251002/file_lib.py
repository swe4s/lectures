import csv
from collections import namedtuple

Ryan = namedtuple('Ryan', ['data', 'header'])


def get_data(file_path, query_value=None, query_col=None, header=False):

    #data = Ryan(data=[], header=[])
    data = []
    header_data = None
    with open(file_path, 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header_data = next(reader)

        for row in reader:
            if query_value and query_col is not None:
                if row[query_col] != query_value: continue

            for i in range(len(row)):
                if row[i] == '...':
                    row[i] = None
            data.append(row)
    if len(data) == 0:
        return None
    else:
        if header:
            return Ryan(data=data, header=header_data)
        else:
            return Ryan(data=data, header=None)

def search_parallel_lists(data_list, index_list, key):
    for index, value in enumerate(index_list):
        if value == key:
            return data_list[index]
