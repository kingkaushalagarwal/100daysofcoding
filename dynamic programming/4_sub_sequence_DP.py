import time
from testInput import input
def findMAX(s1,s2,s3,s4,i,arr):
    # global D
    if i<0:
        if s1==s2 and s3==s4:
            return s1*s3
        else:
            return -1
    if (s1,s2,s3,s4) in D[i]:
        return D[i][(s1,s2,s3,s4)]
    a = findMAX(s1+arr[i],s2,s3,s4,i-1,arr)
    b = findMAX(s1 , s2 + arr[i], s3, s4, i - 1, arr)
    c = findMAX(s1 , s2, s3 + arr[i], s4, i - 1, arr)
    d = findMAX(s1 , s2, s3, s4 + arr[i], i - 1, arr)
    e = findMAX(s1 , s2, s3, s4, i - 1, arr)
    D[i][(s1, s2, s3, s4)]= max(a,b,c,d,e)
    return max(a,b,c,d,e)
#Driver Code
start =time.time()
arr = [7, 7, 3, 3, 10, 9, 4, 3, 3, 4]
D =[{}]*len(arr)
ans = findMAX(0,0,0,0,len(arr)-1 ,arr)
end =time.time()
print(end-start)
print(ans)