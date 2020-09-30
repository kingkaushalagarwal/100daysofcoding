#solution is based on this blog
# from testInput import input
#using dynamic programming for pokeman easy
def pokemamEasy(arr):
    n = len(arr)
    d1 = float('-inf')
    d2 = 0
    for i in range(n):
        temp1 = max(d1, d2 + arr[i])
        temp2 = max(d2, d1 - arr[i])
        d1 = temp1
        d2 = temp2
    print(max(d1, d2))

#Driver Code
for _ in range(int(input())):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    pokemamEasy(arr,q)