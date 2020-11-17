import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', type=str)
parser.add_argument('-c', type=int)

args = parser.parse_args()

print(args.a, args.b, args.c)
