from testInput import input
def toggle(val):
    if val == True:
        return False
    else:
        return True
for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    mark = [False] * n
    check = True
    for i in range(n):
        if arr[0][i] == (i + 1):
            mark[i] = True
        else:
            check = False
    if check == True:
        print(0)
    else:
        flag = False
        count = 0
        for i in range(n - 1, 0, -1):
            if flag:
                mark[i] = toggle(mark[i])

            if mark[i] == True:
                continue
            else:
                mark[i] = True
                flag = toggle(flag)
                count += 1
        print(count )
