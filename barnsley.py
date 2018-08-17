"""
Program to create a barnsley Fern
"""
import random
import matplotlib.pyplot as plt
X = 0.0
Y = 0.0
XL = []
for i in range(100000):
    a = random.random()
    if a < 0.1:
        x1 = 0
        y1 = 0.16*Y
    elif a < 0.7:
        x1 = 0.85*X+0.04*Y
        y1 = -0.04*X+0.85*Y+1.6
    elif a < 0.85:
        x1 = 0.2*X-0.26*Y
        y1 = 0.23*X+0.22*Y+1.6
    else:
        x1 = -0.15*X+0.28*Y
        y1 = 0.26*X+0.24*Y+0.44
    X = x1
    Y = y1
    a = [X, Y]
    XL.append(a)
plt.figure(figsize=(7, 8))
plt.scatter(*zip(*XL), color='g', s=0.2)
plt.show()
