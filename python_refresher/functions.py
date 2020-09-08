def is_equal(a, b, delta=0.0001):
    return abs(a - b) < delta

print(is_equal(0.001,0.002))
print(is_equal(0.001,0.002,delta=0.005))
