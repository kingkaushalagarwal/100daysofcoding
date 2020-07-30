# from testInput import input
def find(arr,i,count,summ,z,flag):
    if count==0:
        # print(summ)
        return summ

    #previous left move
    a = -1;b=-1
    if flag==False and i>0 and z>0:
        a = find(arr, i - 1, count - 1, summ + arr[i - 1], z - 1, True)
    b = find(arr,i+1,count-1,summ+arr[i+1],z,False)
    return max(a,b)


for _ in range(int(input())):
    n,k,z = map(int,input().split())
    arr =  list(map(int,input().split()))
    # ans  = find(arr,0,k,arr[0],z,False)
    # print(n,k,z,arr)
    # print(ans)
    summ = sum(arr[:k])
    l= []
    for i in range(z):
        maxpair =-1
        for i in range(1,k-2):
            maxpair = max(maxpair,arr[i-1]+arr[i])
        l.append(summ + maxpair - ( arr[k-1]+arr[k-2]))
        if k-3>0:
            l.append(summ+arr[k-3]-arr[k-1])
        su