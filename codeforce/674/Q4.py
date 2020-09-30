# from testInput import input
n = int(input())
arr = list(map(int,input().split()))
d = dict()
d[0]=None
summ = 0
count=0
for i in range(n):
    summ = summ + arr[i]
    if summ in d:
        count+=1
        summ = arr[i]
        d = {0:None,arr[i]:None}
    else:
        d[summ]=None
print(count)
