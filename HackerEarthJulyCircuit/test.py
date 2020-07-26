from testInput import input

for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    if 2 * x <= y:
        print(x * n * m)
    else:
        ans = ((n * m) // 2) * y
        if (n * m) & 1 == 0:
            print(ans)
        else:
            print(ans + y)
