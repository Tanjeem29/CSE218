import numpy as np
import matplotlib.pyplot as plt




def regress(xarr, yarr, n):
    xy = 0
    x2 = 0
    xex = 0
    y = 0
    x = 0
    ex = 0
    for i in range(n):
        xy = xy + xarr[i] * yarr[i]
        x2 = x2 + xarr[i] * xarr[i]
        xex = xex + xarr[i] * np.exp(xarr[i])
        y = y + yarr[i]
        x = x + xarr[i]
        ex = ex + np.exp(xarr[i])

    c = [[0],[0]]
    deno = x * xex - x2 * ex
    c[0] = (xex * y - xy * ex)/deno
    c[1] = (xy * x - y * x2) / deno
    return c




def myfunc(x,c):
    return c[0]*x + c[1] * np.exp(x)


def Draw_Regress_ScatterF(f, c, myX, myY):
    # startX = np.amin(myX) - .2
    # # startX = 0
    # endX = np.amax(myX) + .2
    startX = 0
    endX = 2
    x = np.linspace(startX, endX, 101)
    y = f(x, c)
    plt.plot(x, y)
    plt.xlim(startX - 1, endX + 1)
    plt.scatter(A[0], A[1], 10, c = 'red')
    plt.grid()
    plt.show()


A = list()

file1 = open('data.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1

    val = list()
    for s in line.split():
        val.append(float(s))
    A.append(val)

A = np.transpose(A)
n = count
const = regress(A[0], A[1], n)
print("Value of a is: ", const[0], "\nValue of b is: ", const[1])
Draw_Regress_ScatterF(myfunc, const, A[0], A[1])

