import sys

file_name = sys.argv[1]
tissue_name = sys.argv[2]
out_file_name = sys.argv[3]

o = open(out_file_name, 'w')

header = None
sampid_col = -1
smts_col = -1


f = open(file_name)
for l in f:
    A = l.rstrip().split('\t')
    if header is None:
        header = A
        sampid_col = A.index('SAMPID')
        smts_col = A.index('SMTS')
        continue

    if A[smts_col] == tissue_name:
        o.write(A[sampid_col] + '\n')
f.close()
o.close()
