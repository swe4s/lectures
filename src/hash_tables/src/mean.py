import sys
import statistics

V=[]
for l in sys.stdin:
    V.append(float(l))
print(statistics.mean(V))
