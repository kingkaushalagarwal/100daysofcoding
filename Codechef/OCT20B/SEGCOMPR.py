from testInput import input
from math import log,floor
def find(num):
    if num==0:
        return 0
    value =  2**floor(log(num,2))
    # print(num,value)
    return value
#driver code
n = int(input())
arr  = list(map(int,input().split()))
ans  = 0
for i in range(n):
    xor  = 0
    for j in range(i,n):
        xor = xor^arr[j]
        print(find(xor))
        ans += find(xor)
print(ans)
# print(sum(arr))