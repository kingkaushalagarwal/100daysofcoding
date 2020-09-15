import sys
"""
edge cases -
1- continuous 2 zeros
2- starting with zero
3- zero preceeding with digit other than 1 or 2
"""
# from testInput import input
def checkValidity(string):
    if string[0]=='0':
        return False
    prev = string[0]
    for i in range(1,len(string)):
        if string[i]=='0' and (prev not in ['1','2']):
            return False
        prev=string[i]
    return True
# for i in range(int(input())):
for string in sys.stdin:
    n = len(string)
    if checkValidity(string)==False:
        print(0)
        continue
    if n==2:
        print(1)
        continue
    dp =[0]*(n)
    dp[0]=1
    dp[1]=1
    for i in range(2,n):
        if string[i-1]=='0':
            dp[i]=dp[i-2]
        elif string[i-2]=='0':
            dp[i]=dp[i-1]
        else:
            dp[i]=dp[i-1]
            if (int(string[i-2])*10 + int(string[i-1]) )<=26:
                dp[i]+=dp[i-2]
    print(dp[-1])



