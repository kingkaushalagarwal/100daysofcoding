from math import floor,ceil,sqrt
from testInput import input
string = ''.join(input().split(' '))
n = len(string)
fl = floor(sqrt(n))
cl = ceil(sqrt(n))
r = fl
c = cl
if fl!=cl and r*c<n:
    r+=1
answer = []
for i in range(c):
    k = i
    l = []
    print("column ",i)
    for j in range(r):
        k1 = k+j*c
        print("position ",k)
        if k1<len(string):
            l.append(string[k1])
        else:
            l.append(" ")
    answer.append(''.join(l))
ans = " ".join([x.strip(" ") for x in answer])
print(ans)