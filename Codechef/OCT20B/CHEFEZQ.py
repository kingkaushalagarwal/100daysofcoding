from math import floor
from testInput import input
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    actual_query=0
    expected_query=0
    ans = -1
    for i in range(len(arr)):
        expected_query += k
        actual_query += arr[i]
        if actual_query<expected_query:
            ans = i+1
            break
    if ans!=-1:
        print(ans)
    else:
        ans = n
        num = actual_query-expected_query
        ans += floor(num/k)+1
        print(ans)