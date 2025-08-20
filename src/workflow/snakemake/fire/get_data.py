import sys

file_name = sys.argv[1]
country_name = sys.argv[2]
out_file = sys.argv[3]


f = open(out_file, 'w')
for l in open(file_name):
    A = l.rstrip().split(',')
    if A[0] == country_name:
        f.write(str(float(A[2]) + float(A[3])) + '\n')
