import math
import random

a = 1
b = 100
r1 = random.randint(a, b)
r2 = random.randint(a, b)
print(r1, r2, math.gcd(r1, r2))
