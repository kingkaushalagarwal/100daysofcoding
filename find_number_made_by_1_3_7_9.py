#semi-optimized approach fails for large input
from heapq import heapify,heappush,heappop
def find(n):
    count = 0
    arr = [1,3,7,9]
    if n<=9:
        count =0;i=0
        while i<len(arr) and arr[i]<=n:
            count+=1
            i+=1
        return count
    else:
        allowed = [1,3,7,9]
        while len(arr)!=0:
            count+=1
            num = heappop(arr)
            for i in range(4):
                new_num = num*10+allowed[i]
                if new_num<=n:
                    heappush(arr,new_num)
        print()
        return count
#optimized approach run for large input
def GP(a,r,n):
    return (a*(r**n-1))//(r-1)
def find1(n):
    allowed =[9,7,3,1]
    dp =[0]*19
    for i in range(19):
        dp[i]= 4**i
    length = 0
    num =n
    arr= []
    while num!=0:
        d = num%10
        arr.append(d)
        num = num//10
        length+=1
    #reversing the array
    arr = arr[::-1]

    def calculate(arr,i,dp,allowed):
        if i>=len(arr): return 1
        ans = 0
        for j in range(4):
            if arr[i]>allowed[j]:
                ans+= dp[length-i-1]
            elif arr[i]==allowed[j]:
                ans+= calculate(arr,i+1,dp,allowed)
        return ans
    return calculate(arr, 0, dp, allowed) + GP(4,4,length-1)


n = int(input())
ans1 = find1(n)
print(ans1)

