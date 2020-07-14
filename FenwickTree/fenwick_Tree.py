#implementation of fenwick  tree
#query 1 :- find prefix sum from 1 to i
#query2 :- update value at i to +/- v (add v or substract v)

def getSum(BITree,i):
    i=i+1;summ=0
    while i>0:
        summ+=BITree[i]
        i-= i&(-i)
    return summ
def update(BITree,n,i,val):
    i+=1
    while i<=n:
        BITree[i]+=val
        i += i&(-i)


def construct(arr):
    n = len(arr)
    BITree =[0]*(n+1)
    for i in range(n):
        update(BITree,n,i,arr[i])
    return BITree
#Driver code
arr =[1,2,3,4,5,6,7,8,9]
prev =0;prefix1 =[]
for i in range(len(arr)):
    prefix1.append(arr[i]+prev)
    prev += arr[i]
prefix2 =[]
BITree = construct(arr)
for i in range(len(arr)):
    prefix2.append(getSum(BITree,i))
print(prefix1)
print(prefix2)
arr[4]=8
update(BITree,len(arr),3,-4)
print(getSum(BITree,3))
print(BITree)