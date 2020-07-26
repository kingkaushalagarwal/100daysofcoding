from testInput import input
from math import log,floor
def mergeSort(l,r,arr):
    if l<r:
        mid = (l+r)//2
        mergeSort(l,mid,arr)
        mergeSort(mid+1,r,arr)
        merge(l,r,mid,arr)
def merge(l,r,mid,arr):
    # print(arr)
    B=[]
    i=l;j=mid+1
    while i<mid+1 and j<r+1:
        if (arr[i]*(2**(floor(log(arr[j],2))+1))+arr[j])<(arr[j]*(2**(floor(log(arr[i],2))+1))+arr[i]):
            B.append(arr[i])
            i+=1
        else:
            B.append(arr[j])
            j+=1
    while i<mid+1:
        B.append(arr[i])
        i+=1
    while j<r+1:
        B.append(arr[j])
        j+=1
    p=0
    for k in range(l,r+1):
        arr[k]=B[p]
        p+=1
# arr=[66]
# mergeSort(0,len(arr)-1,arr)
# print(arr)
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    d =[0]*n
    for i in range(n):
        d[i] = floor(log(arr[i],2))+1
    # maxx =-1
    # for i in range(n):
    #     for j in range(i+1,n):
    #         maxx = max(maxx,abs((arr[i]*(2**d[j])+arr[j]) - (arr[j]*(2**d[i])+arr[i])))
    mergeSort(0,len(arr)-1,arr)
    v1= (arr[0] * (2 ** (floor(log(arr[-1], 2)) + 1)) + arr[-1])
    v2=(arr[-1]*(2**(floor(log(arr[0],2))+1))+arr[0])
    print(abs(v1-v2))
    # print(maxx)