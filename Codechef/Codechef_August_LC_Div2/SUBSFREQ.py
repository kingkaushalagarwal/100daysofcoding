from testInput import input
from collections import Counter,defaultdict
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
def ncr(n,r,p):
    num = den = 1
    for i in range(r):
        num = num * (n - i)
        den = den * (i + 1)
    return (num%p*expo(den,p-2,p))%p

def findCombination(maxx):
    combination = [[1], [1, 1]]
    for i in range(2, maxx + 1):
        combination.append([0] * (i + 1))
        combination[i][0] = 1
        combination[i][-1] = 1
        for j in range(1, i):
            combination[i][j] = (combination[i - 1][j - 1] + combination[i - 1][j]) % m
    for i in range(len(combination)):
        x = combination[i]
        for j in range(1, len(x)):
            x[j] = (x[j] + x[j - 1]) % m
    return combination

def createCombination(combination,n,p):
    combination[n]= [0]*(n+1)
    combination[n][0]=1
    for r in range(n):
        combination[n][r+1] = (combination[n][r]*(n-r)*expo(r+1,p-2,p))%p
    for i in range(1,n+1):
        combination[n][i]+=combination[n][i-1]


#Driver Code
m  = 10**9+ 7
maxx = float('-inf')
num =[]
array =[]
frequency =[]
maxx = float("-inf")
combination = {0:[1]}
# for _ in range(int(input())):
#     n = int(input())
#     num.append(n)
#     arr  = list(map(int,input().split()))
#     array.append(arr)
#     freq = [0] * (n + 1)
#     for x in arr:
#         freq[x] += 1
#     frequency.append(freq)
#     for x in freq:
#         if x not in unique:
#             unique.add(x)
#             createCombination(combination,x,m)

#creating combination array
# combination = findCombination(maxx)

for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = defaultdict(int)
    ans = [0] * (n + 1)
    # print("freq ", freq)
    # for i in range(len(combination)):
    #     print(combination[i])
    counter = Counter(arr)
    if len(counter)==n:
        for i in range(1, n + 1):
            ans[i] = expo(2,n-i,m)
        print(*ans[1:])
        continue
    keys = sorted(list(counter.keys()))
    freq =[]
    for key in keys:
        value = counter[key]
        freq.append(value)
        if value not in combination:
            createCombination(combination,value,m)
    # print(arr)
    # print(combination)
    # print(keys)
    # print(freq)
    for i in range(len(freq)):
        n1 = freq[i]
        count =0
        for r1 in range(1,n1+1):
            #ncr(n1,r1)
            mul = combination[n1][r1] - combination[n1][r1-1]
            for k in range(len(freq)):
                # print("#: ", i, k, mul, r1)
                if  k==i:
                    continue
                else:
                    n2 = freq[k]
                    if k<i:
                        r2 = min(freq[k],r1-1)

                    elif k>i:
                        r2 = min(freq[k], r1)
                    mul = (mul* combination[n2][r2])%m
                # print("#: ", i, k, mul, r1)
            count =  (count + mul)%m
        ans[keys[i]] =count%m
    print(*ans[1:])
# print(combination)