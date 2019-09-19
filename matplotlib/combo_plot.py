import sys
import matplotlib.pyplot as plt

out_file = 'combo.png'
X = []
Y = []
D = []
for l in sys.stdin:
    A = l.rstrip().split()
    X.append(float(A[0]))
    Y.append(float(A[1]))
    D.append(float(A[0]))
    D.append(float(A[1]))

width=5
height=3
fig = plt.figure(figsize=(width,height),dpi=300)

ax = fig.add_subplot(1,2,1)

ax.plot(X, Y, '.')

ax = fig.add_subplot(1,2,2)

ax.hist(D)


plt.savefig(out_file,bbox_inches='tight')
