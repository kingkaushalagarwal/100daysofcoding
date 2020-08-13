from math import log,ceil,factorial
# n = int(input())
# Python3 function to
# calculate nCr % p
def ncr(n, r, p):
	num = den = 1
	for i in range(r):
		num = (num * (n - i)) % p
		den = (den * (i + 1)) % p
	return (num * pow(den, p - 2, p)) % p


def findX(n):
    value =1
    num = n
    while num>value:
        num-=value
        value*=2
    X = min(value//2,num)+(n-num)//2
    return X
def DistinctHeap(n):
    if n==0:
        return 1
    if n==1:
        return 1
    X = findX(n)
    m = 10*9+7
    return (DistinctHeap(X)%m * DistinctHeap(n-X-1)%m * ncr(n-1,X,m)%m)%m
# for i in range(10):
#     print(DistinctHeap(i))
ans = DistinctHeap(6)
print(ans)