from array import  array
from sys import getsizeof as size

a = array('f',[1.0, 2.0, 3.14])
l = [1.0, 2.0, 3.14]
s = set([1.0, 2.0, 3.14])
t = (1.0, 2.0, 3.14)
print (a, l, s, t)

f = 1.0
print(size(f)*3)
print (size(a), size(l), size(s), size(t))

