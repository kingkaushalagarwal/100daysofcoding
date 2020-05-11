# Codechef
# Everyone loves wine
n = int(input())
arr =[];prefix=[0]*n
for i in range(n):
    arr.append(int(input()))
prev =0
for i in range(n):	
    prefix[i]=arr[i]+prev 
    prev = prefix[i]
    
dp =  [[0]*n for i in range(n)]	
for a in range(n):
    for b in range(n-a):
        i=b ;j=a+b
        if i==j:
            dp[i][j] = arr[i]
        else:
            num1 = prefix[j]-prefix[i]
            if i-1>=0:
                num2= prefix[j-1]-prefix[i-1]
            else:
                num2 = prefix[j-1]
            dp[i][j] = max(arr[i]+ dp[i+1][j] + num1 , dp[i][j-1] + num2 + arr[j])
# for i in range(n):
#     print(dp[i])
print(dp[0][-1])			