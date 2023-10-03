import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_file = sys.argv[1]
country = sys.argv[2]
out_file = sys.argv[3]

D = []
for l in open(data_file):
    D.append(float(l))

fig, ax = plt.subplots()
ax.hist(D)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Fires')
ax.set_ylabel('Freq.')
ax.set_title(country)

plt.savefig(out_file,bbox_inches='tight')
