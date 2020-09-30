# from testInput import input
n = int(input())
a = list(map(int,input().split()))
b= list(map(int,input().split()))
minimum = 0
if (b[0]+b[2]<a[0]):
    minimum += abs(b[0]+b[2]-a[0])
if (b[0]+b[1]<a[1]):
    minimum += abs(b[0]+b[1]-a[1])
if (b[1]+b[2]<a[2]):
    minimum += abs(b[1]+b[2]-a[2])
maximum  = 0
maximum += min(a[0],b[1])
maximum += min(a[1],b[2])
maximum += min(a[2],b[0])
print(minimum,maximum)
