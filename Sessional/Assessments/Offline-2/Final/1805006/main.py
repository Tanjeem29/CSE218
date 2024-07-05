import numpy as np


def GaussianElimination(A, B, d=True):
    A = np.array(A)
    B = np.array(B)
    C = np.concatenate((A, B), 1)
    n = np.size(A, 0)
    solu = np.zeros(n)
    for i in range(n):
        if C[i, i] == 0:
            for k in range(i + 1, n):
                if C[k, i] != 0:
                    print("-------------\nPivot == 0")
                    print('Old Matrix:')
                    print('A:')
                    a = C[:, :-1]
                    print(a)

                    print('B:')
                    b = np.transpose([C[:, -1]])
                    print(b)

                    C[[i, k], :] = C[[k, i], :]

                    print('New Matrix:')
                    print('A:')
                    a = C[:, :-1]
                    print(a)

                    print('B:')
                    b = np.transpose([C[:, -1]])
                    print(b)
                    break
        for j in range(i + 1, n):
            deno = float(C[i, i])
            num = float(C[j, i])
            C[j, i:] -= C[i, i:] * num / deno

            if d:
                print('------------------')
                print('Sub-step: ', i + 1, '.', j - i)

                print('A:')
                a = C[:, :-1]
                print(a)

                print('B:')
                b = np.transpose([C[:, -1]])
                print(b)
                print('-------------------')

    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum = sum + solu[j] * C[i, j]
        solu[i] = (C[i, n] - sum) / C[i, i]
    solu = [solu]
    return np.transpose(solu)


n = int(input('No. of Variables:'))
A = list()
B = list()
for i in range(n):
    val = list()
    for s in input().split():
        val.append(float(s))
    A.append(val)

for i in range(n):
    val = list()
    x = input()
    while x == '':
        x = input()
    val.append(float(x))
    B.append(val)

answer = GaussianElimination(A, B)
np.set_printoptions(4)
print('The solution is:')
print(answer)
print(A)
print(B)
# 4
# 1 2 -1 1
# -1 1 2 -1
# 2 -1 2 2
# 1 1 -1 2
# 6
# 3
# 14
# 8

# 4
# 1 2 -1 1
# 1 2 2 3
# 1 2 3 4
# 1 1 -1 2
# 6
# 23
# 30
# 8
