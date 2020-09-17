from math import sqrt
def seive(a,n):
    prime = [True]*(n+1)
    for i in range(2,int(sqrt(n))+1):
        if prime[i]==True:
            for j in range(i*i,n+1,i):
                prime[j]=False
    prime_number=[]
    for i in range(max(2,a),n+1):
        if prime[i]==True:
            prime_number.append(i)
    return prime_number
def solve(a,b):
    n1=a*b
    n2 = (a/2)*(b/2)
    prime = seive(a,b)
    for i in range(len(prime)):
        for j in range(i+1,len(prime)):
            value = prime[i]*prime[j]
            if value>n2 and value<n1:
                print(prime[i],",",prime[j],sep="")

a = int(input())
b = int(input())
# prime = seive(a,b)
# print(prime)
solve(a,b)
#
# 11 13
# 11 17
# 11 19
# 11 23
# 13 17
# 13 19
# 13 23
# 11,13
# 11,17
# 11,19
# 11,23
# 13,17
# 13,19
# 13,23