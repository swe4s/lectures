import csv

def get_data(file_path, query_value=None, query_col=None):
    data = []

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
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
        return data


