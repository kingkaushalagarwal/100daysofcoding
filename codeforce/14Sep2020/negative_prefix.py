# from testInput import input
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    lock = list(map(int,input().split()))
    ans =[]
    hold =[]
    for i in range(n):
        if lock[i]==0:
            hold.append(arr[i])
    hold.sort(reverse=True)
    k=0
    for i in range(len(arr)):
        if lock[i]==1:
            ans.append(arr[i])
        else:
            ans.append(hold[k])
            k+=1
    # print(arr,lock)
    print(*ans)