from copy import deepcopy
from testInput import input


def processing(array, n):
    if len(array) > 1:
        for i in range(n):
            array[-1][i] += array[-2][i]


def maxLexogriphicalValue(maxx, array, n):
    ind = maxx[0]
    for i in range(n):
        if array[ind][i] < array[-1][i]:
            maxx[0] = len(array) - 1


def firstQuery(lights, L, R):
    # print("L R",L,R)
    for i in range(L, R + 1):
        lights[i] = lights[i] ^ 1
    return lights


def SecondQuery(array, A, B, L, R, n):
    # print(array)
    count = [0] * n
    A -= 1
    if A >= 0:
        first = -1
        c = 0
        for i in range(L, R + 1):
            count[i] = array[B][i] - array[A][i]
            if count[i] % 2 == 1:
                if first == -1:
                    first = i
                c += 1
        if first == -1:
            return "0 0"
        else:
            return str(c) + " " + str(first + 1)
    else:
        c = 0
        first = -1
        for i in range(L, R + 1):
            if array[B][i] % 2 == 1:
                if first == -1:
                    first = i
                c += 1
        if first == -1:
            return "0 0"
        else:
            return str(c) + " " + str(first + 1)


for _ in range(int(input())):
    n, m = map(int, input().split())
    lights = 0
    array = []
    flag = False
    maxx = [-1]
    for i in range(m):
        query = list(map(int, input().split()))
        if query[0] == 1:
            L, R = query[1] - 1, query[2] - 1
            lights = firstQuery(lights, L, R)
            array.append(deepcopy(lights))

            if flag == False:
                maxx[0] = (i + 1)
                flag = True
            else:
                maxLexogriphicalValue(maxx, array, n)
            processing(array, n)

        # print("lights: ",i,lights)
        elif query[0] == 2:
            array.append(deepcopy(lights))
            processing(array, n)

            A, B, L, R = query[1:]
            A, B = A - 1, B - 1
            L, R = L - 1, R - 1
            if flag == False:
                print("0 0")
            else:
                ans = SecondQuery(array, A, B, L, R, n)
                print(ans)
        else:
            array.append(deepcopy(lights))
            processing(array, n)
            if flag == False:
                print(0)
            else:
                print(maxx[0])
