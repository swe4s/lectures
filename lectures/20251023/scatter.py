import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_file = sys.argv[1]
out_file = sys.argv[2]
title = sys.argv[3]
x=sys.argv[4]
y=sys.argv[5]

X = []
Y = []
for l in open(data_file):
    A = l.rstrip().split()
    X.append(float(A[0]))
    Y.append(float(A[1]))

fig, ax = plt.subplots()
ax.scatter(X,Y)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(title)

plt.savefig(out_file,bbox_inches='tight')
