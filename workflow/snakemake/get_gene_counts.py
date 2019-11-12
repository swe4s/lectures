import sys
import gzip

file_name = sys.argv[1]
gene_name = sys.argv[2]

out_file_name = gene_name + '_counts.txt'

o = open(out_file_name, 'w')

version = None
dim = None
header = None

f = gzip.open(file_name, 'rt')
for l in f:
    A = l.rstrip().split('\t')
    if version is None:
        version = A
        continue
    if dim is None:
        dim = A
        continue
    if header is None:
        header = A
        continue
    if A[1] == gene_name:
        for i in range(2, len(header)):
            o.write(header[i] + ' ' + A[i] + '\n')
f.close()
o.close()
