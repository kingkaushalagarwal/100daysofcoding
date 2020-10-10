
# from testInput import input
def check(arr):
    for i in range(len(arr)):
        if arr[i]!=0:
            return True
    return False


#Driver Code
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    #base case when array element is zero
    if len(arr)==0:
        print("YES")
        print()
        continue
    if check(arr)==False or sum(arr)==0:
        print("NO")
    else:
        arr.sort(reverse=True)
        while arr[0]==0:
            arr.sort()
        if arr[0]==0 and arr[-1]==0:
            print("NO")
        else:
            print("YES")
            print(*arr)
