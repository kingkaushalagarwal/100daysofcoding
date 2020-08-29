from testInput import input
from collections import Counter

for _ in range(int(input())):
    n, edge = map(int, input().split())
    arr = list(map(int, input().split()))
    # if edge >= n:
    #     print(0)
    #     continue
    if n == 1:
        if arr[0] == 1:
            print(1)
        else:
            print(0)
        continue
    maxx = max(arr)
    dp = [0] * (maxx + 1)
    freq = [0] * (maxx + 1)
    for x in arr:
        freq[x] += 1
    dp[1] = freq[1]
    m = 10 ** 9 + 7
    max_edge = freq[1] + (freq[1]*(freq[1]-1))//2
    for i in range(2, len(freq)):
        dp[i] = (dp[i - 1] * freq[i])
        max_edge += (freq[i-1]*freq[i]) + (freq[i]*(freq[i]-1))//2

    if edge>max_edge:
        print(0)
    else:
        print(dp[-1] % m)
