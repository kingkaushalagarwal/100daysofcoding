from testInput import input
import sys
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    prev = sys.maxsize
    pre =[0]*len(arr)
    post = [0]*len(arr)
    for i in range(len(arr)):
        pre[i]= min(arr[i],prev)
        prev = pre[i]

    prev = sys.maxsize
    for i in range(len(arr)-1,-1,-1):
        post[i] = min(arr[i],prev)
        prev = post[i]
    flag = False
    # print(arr)
    # print(pre)
    # print(post)
    # print(arr)
    for i in range(1,len(arr)-1):
        if pre[i]<arr[i] and post[i]<arr[i]:
            print("YES")
            print(pre[i],arr[i],post[i])
            print(arr.index(pre[i]),i,arr.index(post[i]))
            flag = True
            break
    if flag==False:
        print("NO")
