# from testInput import input
def find(i,arr,flag):
    if i==len(arr):
        return 0
    #friends turn
    c = 0
    if flag==1:
        if arr[i]==1:
            c =1
        return c + min(find(i+1,arr,1,1) , find(i+1,arr,0,1))

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    count =0
    i=0
    flag = 1
    while i<n:
        if flag==1:
            if arr[i]==1:
                count+=1
            i+=1
            if (i)<n and arr[i]==0:
                i+=1
            flag = 0
        else:
            i+=1
            if (i)<n and arr[i]==1:
                i+=1
            flag = 1
    print(count)

# 2
# 2
# 2
# 2
# 1
# 0
