import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


D = []
for l in open(sys.argv[1]):
    D.append(int(l))

width=4
height=3
fig = plt.figure(figsize=(width,height),dpi=300)

ax = fig.add_subplot(1,1,1)
ax.plot(D)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig(sys.argv[2],bbox_inches='tight')
