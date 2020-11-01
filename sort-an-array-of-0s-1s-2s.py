#dutch national flag problem.
from testInput import input
def check(arr):
    for x in arr:
        if x not in [0,1,2]:
            return False
    return True
def sortArray(arr):
    l,m,h=0,0,len(arr)-1
    while m<=h:
        if arr[m]==0:
            arr[l],arr[m] = arr[m],arr[l]
            l+=1
            m+=1
        elif arr[m]==1:
            m+=1
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1


print("Enter the array of 0's , 1's and 2's")
arr = list(map(int,input().split()))
if check(arr)==False:
    print("Input array is invalid")
else:
    sortArray(arr)
    print(arr)
