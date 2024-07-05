import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def f(arr):
    a = np.array(arr)
    # print(a, ' ', np.size(a,1))
    if np.size(a, 1) == 1:
        return arr[1][0]
    else:
        return (f(arr[:, :-1]) - f(arr[:, 1:])) / (arr[0, 0] - arr[0, -1])


def findClosestPoints(x, arr, num):
    a = np.array(arr)
    n = np.size(a, 1)
    max = 0
    min = n
    temp = np.array(a[0][:])
    for i in range(num):
        index1 = (np.abs(temp - x)).argmin()  # find index of x in temp nearest to given x
        index = np.searchsorted(a[0][:], temp[index1])  # find index of x in a nearest to given x
        # print('temp: ', temp, ',  index1: ', index1)
        # print('a: ', A, ',  index: ', index)

        if index >= max:
            max = index
        if index <= min:
            min = index
        temp = np.delete(temp, index1)
    return [min, max + 1]


def polynomialx(x, arr, num):
    a = np.array(arr)
    n = np.size(a, 1)
    y = 0
    closest = findClosestPoints(x, arr, num)
    # print(range(closest[0], closest[1]))
    product = 1
    for i in range(closest[0], closest[1]):
        y = y + product * f(arr[:, closest[0]:(i + 1)])
        product = product * (x - a[0, i])
        #print(i, ':  ', f(arr[:, :(i + 1)]), 'y: ', y)

    return y


def NewtonwithRelError(x, arr, num):
    li = list()
    relErr = 'NA'
    yp = 'NA'
    y = 0
    A = np.array(arr)
    for i in range(0, num):
        y = polynomialx(x, A, i+1)
        if i > 0:
            relErr = np.abs(yp - y) / y * 100
        li.append([i+1, yp, y, relErr])
        yp = y
    print(tabulate(li, ['Iteration', 'Previous y', 'Current y', 'Relative Error'], 'fancy_grid'))
    return y


# def polycoeff(x,arr,num)
#     closest = findClosestPoints(x, arr, num)
#     y =np.zeros(5)
#     for i in range(closest[0],closest[1]):
#         y[i] = f(arr[:, closest[0]:(i+1)])
#
#     xs = np.zeros(6)
#     xp = 1
#     for i in range[closest[0],closest[1]]:
#         xs[0]= xs[0] + x[i]
#         xp = xp * x[i]
#     for i in range[closest[0],closest[1]-1]:
#         xs[1]= xs[0] + x[i]
#     for i in range[closest[0],closest[1]-2]:
#         xs[2]= xs[0] + x[i]
#     for i in range[closest[0],closest[1]]:
#         xs[5]= xp/ x[i]


n = int(input('No. of points for mass:'))
A = list()
for i in range(n):
    val = list()
    for s in input().split():
        val.append(float(s))
    A.append(val)
A = np.transpose(A)

n2 = int(input('No. of points for velocity:'))
A2 = list()
for i in range(n2):
    val = list()
    for s in input().split():
        val.append(float(s))
    A2.append(val)
A2 = np.transpose(A2)


# x = int(input('Enter x:'))
# pts = int(input('Enter number of closest points:'))
# print(findClosestPoints(x, A, pts))
x = 25
pts = 5
ans = NewtonwithRelError(x, A, pts)
ans2 = NewtonwithRelError(x, A2, pts)

xin = np.linspace(.1,40.1,40)
ymass = np.array(xin)
yvel = np.array(xin)
for i in range(40):
    ymass[i] = polynomialx(xin[i], A, pts)
    yvel[i] = polynomialx(xin[i], A2, pts)

plt.plot(xin,ymass, '-bo')
plt.plot(xin,yvel, '-ro')
plt.legend(["Mass (in metric ton) vs time (in sec)", "Velocity (in m/sec) vs time (in sec)"])
plt.show()



print('mass=', ans, ' metric tons')
print('velocity=', ans2, ' m/sec')




# 11
# 0 1011
# 5 1255
# 9 1347
# 12 1101
# 19 1203
# 22 1245
# 26 1378
# 28 1315
# 30 1475
# 33 1547
# 40 1689
# 11
# 0 1000
# 5 1500
# 9 2000
# 12 2500
# 19 3000
# 22 3500
# 26 4000
# 28 4500
# 30 5000
# 33 5500
# 40 6000