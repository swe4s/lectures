
def get_data(file_name, query_value=None, query_col=None, header=False):
    _header = []
    data = []
    with open(file_name) as lines:
        for line in lines:
            if query_value is None or query_col is None:
                data.append(line)
            else:
                if len(_header) == 0:
                    _header = line.rstrip().split(',')
                    continue
                fields = line.rstrip().split(',')
                if fields[query_col] == query_value:
                    data.append(line)
    if header:
        return data, _header
    else:
        return data
