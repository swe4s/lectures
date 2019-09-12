import sys


def is_even(n):
    try:
        return n % 2 == 0
    except TypeError:
        raise TypeError('ERROR: given value type is not supported')


def main():
    try:
        n = int(sys.argv[1])
    except ValueError:
        sys.exit('ERROR: Argument must be an int')
    except IndexError:
        sys.exit('ERROR: Missing int')

    if is_even(n):
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
