from testInput import input

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = []
    for i in range(n):
        l.append(input())
    maxx = 0

    for i in range(n):
        count = 0
        count1 = 0
        for j in range(m):
            if l[i][j] == '#' and ((i - 1) < 0 or l[i - 1][j] == '.'):
                count += 1
            else:
                count = 0
            if l[i][j] == '#' and ((i + 1) >= n or l[i + 1][j] == '.'):
                count1 += 1
            else:
                count1 = 0
            maxx = max(maxx, count, count1)

    for j in range(1, m):
        count = 0
        count1 = 0
        for i in range(n):
            if l[i][j] == '#' and ((j - 1) < 0 or l[i][j - 1] == '.'):
                count += 1
            else:
                count = 0
            if l[i][j] == '#' and ((j + 1) >= m or l[i][j + 1] == '.'):
                count1 += 1
            else:
                count1 = 0
            maxx = max(maxx, count, count1)
    print(maxx)