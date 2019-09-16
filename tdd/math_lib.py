

def list_mean(L):

    if L is None:
        return None

    if len(L) == 0:
        return None

    s = 0

    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Cannot find mean. Unsupported value in list.')
        s += l

    return s/len(L)

def read_file_col(file_name, col_num):

    try:
        f = open(file_name)
    except FileNotFoundError:
        raise FileNotFoundError(file_name + ' not found.')

    num = 0

    L = []

    for l in f:
        A = l.rstrip().split(',')
        try:
            L.append(int(A[col_num]))
        except IndexError:
            f.close()
            return None
        num += 1

    f.close()

    if num == 0:
        return None

    return L
