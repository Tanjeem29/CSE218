import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def func(t):
    g = 9.8
    m0 = 140000
    q = 2100
    u = 2000
    return u * np.log(m0 / (m0 - q * t)) - g * t


def trapezoid(f, t0, t1, n):
    diff = t1 - t0
    h = diff / n
    sum = 0
    for i in np.linspace(t0, t1, n + 1):
        if i == t0 or i == t1:
            sum = sum + f(i)
        else:
            sum = sum + 2 * f(i)

    return sum * h / 2


def presettrapezoid(f, t0, t1, n):
    ans = list()
    relErr = 'NA'
    prev = 'NA'
    ans.append(['0', '----', '----', '----'])

    for i in range(n):
        curr = trapezoid(f, t0, t1, i + 1)
        if i > 0:
            relErr = abs((curr - prev)) / curr * 100

        ans.append([i + 1, prev, curr, relErr])
        prev = curr
    print('-------------------------------------------------------------')
    print('For Trapezoid Rule: ')
    print(tabulate(ans, ['n', 'Previous Answer', 'Current Answer', 'Relative Error'], 'fancy_grid'))
    print('-------------------------------------------------------------')


def presetsimpson(f, t0, t1, n):
    ans = list()
    relErr = 'NA'
    prev = 'NA'
    curr = 'NA'
    ans.append(['0', '----', '----', '----'])
    for i in range(n):
        curr = simpson(f, t0, t1, i + 1)
        if i > 0:
            relErr = abs((curr - prev)) / curr * 100
        ans.append([i + 1, prev, curr, relErr])
        prev = curr

    print('-------------------------------------------------------------')
    print('For Simpson''s 1/3rd Rule: ')
    print(tabulate(ans, ['n', 'Previous Answer', 'Current Answer', 'Relative Error'], 'fancy_grid'))
    print('-------------------------------------------------------------')


def simpsonsingle(f, t0, t2):
    return (t2 - t0) * (f(t0) + f(t2) + 4 * f((t0 + t2) / 2)) / 6


def simpson(f, t0, t1, n):
    h = (t1 - t0) / n
    sum = 0
    for i in range(n):
        sum = sum + simpsonsingle(f, t0 + i * h, t0 + (i + 1) * h)

    return sum


x0 = 8
x1 = 30
presettrapezoid(func, x0, x1, 5)
presetsimpson(func, x0, x1, 5)
N = int(input('Enter n: '))
print('Distance covered:')
print('By using Trapezoid rule : ', trapezoid(func, x0, x1, N), ' m')
print('By using Simpson''s 1/3rd rule : ', simpson(func, x0, x1, N), ' m')
