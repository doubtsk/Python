from random import random
from math import sqrt
from time import perf_counter

darts = 1200
hits = 0
t1 = perf_counter()
for i in range(1, darts):
    x, y = random(), random()
    dist = sqrt(x**2+y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4*(hits/darts)
t2 = perf_counter()
print(("Pi的值 %s" % pi))
print("程序运行时间是 %-5.5fs" % (t2-t1))
