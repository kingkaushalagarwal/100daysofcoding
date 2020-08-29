from testInput import input
for _ in range(int(input()))
    n,m = map(int,input())
    arr= list(map(int,input().split()))
    if arr[0]==1:
        print(-1)
        continue
    i=0
    while arr[i]==-1:
        i+=1
    left = i
    j=n-1
    while arr[j]==-1:
        j-=1
    right = j
    if i+1<j and i<n:
        last = arr[i]
        count=0
        for k in range(i+1,j+1):
            if arr[k]==-1:
                count+=1
            else:
                if prev==-1:
                    if abs(last-arr[i]) >=count:
                        ans=0
                    else:
                        ans = count//
