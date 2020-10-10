from testInput import input
def findLargerCount(arr,value,l,r):
    """
    for finding the count of numbers greater than value in between given range
    :param arr:
    :param value:
    :param l:
    :param r:
    :return:
    """
    count=0
    for i in range(l,r):
        if arr[i]>x:
            count+=1
    return count

def findSmallerCount(arr,value,l,r):
    """
    find count of numbers smaller than given value in specified range
    :param arr:
    :param value:
    :param l:
    :param r:
    :return:
    """
    count = 0
    for i in range(l,r):
        if arr[i]<x:
            count+=1
    return count

#Driver Code
for _ in range(int(input())):
    n,x,p,k = map(int,input().split())
    p,k = p-1,k-1
    arr = list(map(int,input().split()))
    arr.sort()
    ans=-1000
    #when pth smallest element is equal to X
    if arr[p]==x:
        ans = 0
    #creating required array is not possible
    elif (k>p and arr[p]<x) or (k<p and arr[p]>x):
        ans = -1
    else:
        if k>p:
            ans = findLargerCount(arr,x,0,p+1)
        elif k<p :
            ans = findSmallerCount(arr,x,p,n)
        elif k==p:
            if arr[p]>x:
                ans = findLargerCount(arr, x, 0, p + 1)
            else:
                ans = findSmallerCount(arr, x, p, n)
    print(ans)

