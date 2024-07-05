import math
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def draw(x, y):
    plt.plot(x, y)


def f(var):
    return k - (var / (1 - var)) * np.sqrt(2 * pt / (2 + var))


def bisect1(lo, hi, err, maxIt):
    it = 1
    xl = lo
    xh = hi
    relErr = 300
    xp = 0
    xm = 0
    while it <= maxIt:
        xm = (xl + xh) / 2
        if f(xm) * f(xl) < 0:
            xh = xm
        else:
            xl = xm

        if it > 1:
            relErr = abs((xp - xm) / xm) * 100
            if relErr < err:
                break

        xp = xm
        it = it + 1
    return xm


def bisect2(lo, hi, err, maxIt):
    it = 1
    xl = lo
    xh = hi
    relErr = "NA"
    xp = "NA"
    xm = 0
    li = list()

    while it <= maxIt:
        xm = (xl + xh) / 2

        if f(xm) * f(xl) < 0:
            xh = xm
        else:
            xl = xm

        if it > 1:
            relErr = abs((xp - xm) / xm) * 100
            subl = [it, xm, relErr]
            li.append(subl)
            if relErr < err:
                break
        else:
            subl = [it, xm, relErr]
            li.append(subl)




        xp = xm
        it = it + 1

    headers = ['Iteration', 'Xm', 'Relative Error']
    print(tabulate(li, headers, "fancy_grid"))


##Constants
start = -1
end = 5
numpt = 101
k = 0.05
pt = 3
roundto = 5

x = np.linspace(start, end, numpt)
y = f(x)
# y = np.array(x)
# for i in range(numpt):
#     y[i] = k - (x[i] / (1 - x[i])) * math.sqrt(2 * pt / (2 + x[i]))
y[:-1][np.diff(y) > 0] = np.nan
# P=np.where(np.isinf(y))

x2 = np.array([start, end])
y2 = np.array([0, 0])
y3 = np.array([-20, 30])
plt.axes([.09, .09, .8, .8])

plt.plot(x, y)
plt.plot(x2, y2)
plt.plot(y2, y3)
plt.text(4.5, -3, 'x-axis')
plt.text(-.6, 30, 'y-axis')
plt.text(1.05, -15, 'y=f(x)')


ans = round(bisect1(-.3, .7, .5, 20), roundto)
print('Approximate Solution upto', roundto, 'decimal places:', ans)

bisect2(-.3, .7, .5, 20)
plt.show()
