import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out_file = 'hist.png'
D = []
for l in sys.stdin:
    A = l.rstrip().split()
    D.append(float(A[0]))
    D.append(float(A[1]))

width=3
height=3
fig = plt.figure(figsize=(width,height),dpi=300)

ax = fig.add_subplot(1,1,1)

ax.hist(D)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig(out_file,bbox_inches='tight')
