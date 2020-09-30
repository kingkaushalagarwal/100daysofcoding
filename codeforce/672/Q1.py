# from testInput import input
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if len(set(arr))<n :
        print("YES")
    else:
        flag = False
        prev=  float('inf')
        for i in  range(n):
            if prev<arr[i]:
                flag = True
                break
            prev = arr[i]
        if flag:
            print("YES")
        else:
            print("NO")