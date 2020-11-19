import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out_file = 'scatter.png'
X = []
Y = []
for l in sys.stdin:
    A = l.rstrip().split()
    X.append(float(A[0]))
    Y.append(float(A[1]))

width=3
height=3
fig = plt.figure(figsize=(width,height),dpi=300)

ax = fig.add_subplot(1,1,1)

ax.plot(X, Y, '.')

ax.set_ylabel("Y axis")
ax.set_xlabel("X axis")

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig(out_file,bbox_inches='tight')
