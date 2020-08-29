from testInput import input
# from testInput import input
def check(arr,t,d):
    st = arr[0]
    count=len(arr)-1
    for i in range(1,n):
        while (st+t)<arr[i]:
            st+=t
        st +=t
        if st>(arr[i]+d):
            return False
    return True


for _ in range(int(input())):
    n,d = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    if n==2:
        print(arr[1]+d-arr[0])
        continue
    minn= arr[0]
    maxx= max(arr)+d
    l = 0
    h = (maxx-minn+1)/(n-1)
    ans =0
    while l<=h:
        mid = (l+h)/2
        if check(arr,mid,d)==False:
            h=mid-0.00001
        else:
            ans=mid
            l=mid+0.00001
    print(float(ans))