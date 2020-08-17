# #
def expo(x,n,p):
    if n==0:
        return 1
    elif n==1:
        return x%p
    elif n&1: #odd
        return (x%p * expo((x*x)%p, n//2,p))%p
    else: #even
        return expo((x * x) % p, n // 2, p) % p

#Driver Code
a,b = map(int,input().split())
k = int(input())
# a,b,k= 1,10,3
p = 10**9+7
if a>b:
    a,b = b,a
#both odd
if a&1 and b&1:
    e = (b-a)//2
    o = e+1
elif a&1==0 and b&1==0:
    o = (b-a)//2
    e = o+1
else:
    e = (b-a+1)//2
    o = e
# print(o,e)
first = expo(e+o,k,p)
flag = 1
if (e-o)<0 and k&1==1:
    flag = -1

second = expo(abs(e-o),k,p)
# print(first,second*flag)
ans = (first + second*flag)//2
# ans = (expo(first,k,p) + expo(second , k, p))//2
print(ans)