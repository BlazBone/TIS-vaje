from functools import reduce
from math import log2

p = [2/3, 1/3]

h = -sum([p_i*log2(p_i) for p_i in p])
print(h)
