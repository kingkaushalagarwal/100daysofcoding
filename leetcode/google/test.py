from testInput import input
n,m = map(int,input().split())
arr =[]
for i in range(n):
    arr.append(input())
column=[0]*m
row =[0]*n
for _ in range(int(input())):
    l = list(map(int,input().split()))
    x1,y1,x2,y2 = [x-1 for x in l]
    row[x1]+=1
    if x2+1<n:
        row[x2+1]-=1
    column[y1]+=1
    if y2+1<m:
        column[y2+1]-=1
    print(row)
    print(column)
print("dsfaf")
for i in range(1,len(row)) :
    row[i]+=row[i-1]
for j in range(1,len(column)):
    column[j]+=column[j-1]
ans =[[0]*m for i in range(n)]
for i in range(n):
    print(ans[i])

for i in range(n):
    for j in range(m):
        print(arr[i][j])
        ans[i][j]=int(arr[i][j])
        if row[i]&1 or column[j]&1:
            ans[i]=ans[i]^1

# for i in range(n):
#     print(ans[i])
#
# print(row)
# print(column)