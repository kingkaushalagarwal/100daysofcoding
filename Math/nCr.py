from math import factorial as fact
def expo(x,n,p):
    if n==0:
        return 1
    elif n==1:
        return x%p
    elif n&1:
        return ((x%p)*expo((x*x)%p,n//2,p)%p)
    else:
        return expo((x*x)%p,n//2,p)%p

#most optimize way
# def ncr(n,r,p):
#     num = den = 1
#     for i in range(r-1):
#         num = num * (n - i)
#         den = den * (i + 1)
#     print(num,den)
#     return (num%p*expo(den,p-2,p))%p

#finding ncr without module
def ncr1(n,r):
    num=den=1
    for i in range(r):
        num = num*(n-i)
        den = den*(i+1)
    return num//den
def ncr(n, r, p):
    # initialize numerator
    # and denominator
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * expo(den, p - 2, p)) % p

#using factorial function
# def ncr2(n,r):
#     return fact(n)//(fact(n-r)*fact(r))
# p  = 10**9+ 7
# for i in range(6+1):
#     print(ncr(6,i,p),ncr1(6,i),ncr2(6,i))
print(ncr(5,2,13))