import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def f(x):
    pi = 3.1416
    r = 3
    return (pi * x * x * (3 * r - x)) / 3 - 4


def DrawF(f, Start, End):
    x = np.linspace(Start, End, 101)
    y = f(x)
    plt.plot(x, y)
    plt.plot([Start, End], [0, 0])
    plt.plot([0, 0], [-10, 100])
    plt.xlim(Start - 1, End + 1)
    plt.show()


def bisect(f, hi, lo, minErr, maxIt):
    it = 1
    xl = lo
    xh = hi
    xm = 0
    relErr = 'NA'
    xp = 'NA'
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
            li.append([it, round(xp, 6), round(xm, 6), round(relErr, 6)])
            if relErr < minErr:
                break
        else:
            li.append([it, xp, xm, relErr])

        xp = xm
        it = it + 1
    print(tabulate(li, ['Iteration', 'Previous X', 'Current X', 'Relative Error %']))
    return xm


glo = float(input('Enter lower x for graph: '))
ghi = float(input('Enter higher x for graph: '))
DrawF(f, -4, 4)
lo = float(input('Enter lower x for bisection: '))
hi = float(input('Enter higher x for bisection: '))
err = float(input('Enter minimum Error tolerance: '))
it = int(input('Enter Maximum iterations: '))

print('Required height is :', round(bisect(f, hi, lo, err, it), 6), 'feet')
