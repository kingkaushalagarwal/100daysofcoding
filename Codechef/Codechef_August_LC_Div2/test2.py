def expo(x,n,p):
    if n==0:
        return 1
    elif n==1:
        return x%p
    elif n&1:
        return ((x%p)*expo((x*x)%p,n//2,p)%p)
    else:
        return expo((x*x)%p,n//2,p)%p

def createCombination(combination,n,p):
    combination[n]= [0]*(n+1)
    combination[n][0]=1
    for r in range(n):
        combination[n][r+1] = (combination[n][r]*(n-r)*expo(r+1,p-2,p))%p
    for i in range(1,n+1):
        combination[n][i]+=combination[n][i-1]



p  = 10**9+7
combination ={0:[1]}
for i in range(1,5+1):
    createCombination(combination,i,p)
for i in range(5+1):
    print(combination[i])