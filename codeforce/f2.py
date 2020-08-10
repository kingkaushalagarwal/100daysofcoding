# from testInput import input
for _ in range(int(input())):
    n,m = map(int,input().split())
    arr =[]
    # print(n,m)
    for i in range(n):
        arr.append(input())
        # print(arr[i])
    count =0

    for i in range(n):
        if arr[i][m-1]=='R':
            count+=1
    for i in range(m):
        if arr[n-1][i]=='D':
            count+=1
    print(count)
