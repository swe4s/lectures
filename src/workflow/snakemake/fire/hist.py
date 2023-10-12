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

D = []
for l in open(data_file):
    D.append(float(l))

fig, ax = plt.subplots()
ax.hist(D)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(title)

plt.savefig(out_file,bbox_inches='tight')
