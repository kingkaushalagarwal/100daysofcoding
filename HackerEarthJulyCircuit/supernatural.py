n = int(input())
l =[  11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
d = dict().fromkeys(l,None)
dp=[0]*101
dp[0]=0
dp[1]=0
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=1
dp[6]=3
dp[7]=1
dp[8]=4
dp[9]=2
for i in range(10,101):
    if i in d:
        continue
    summ=0
    for j in range(2,10):
        if i%j==0:
            summ+=dp[i//j]
    dp[i] = summ
print(dp[n])
