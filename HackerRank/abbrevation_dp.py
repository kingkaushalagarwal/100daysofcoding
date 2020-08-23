from testInput import input
def abbreviation(a, b):
    a = a.upper()
    n = len(a)
    m = len(b)
    lcs = [[0]*(m+1) for i in range(n+1)]
    dp  = [[0]*(m+1) for i in range(n+1)]
    #1- diagonal 2- left 3-up
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+1
                dp[i][j]=1
            else:
                #left
                if lcs[i][j-1] >=lcs[i-1][j]:
                    lcs[i][j]=lcs[i][j-1]
                    dp[i][j]=2
                #up
                else:
                    lcs[i][j]=lcs[i-1][j]
                    dp[i][j]=3
    i=n;j=m
    string =[]
    # for i in range(len(lcs)):
    #     print(lcs[i])
    for i in range(len(lcs)):
        print(dp[i])

    while i>=0 and j>=0:
        if dp[i][j]==1:
            string.append(a[i-1])
            i-=1;j-=1
        #move left
        elif dp[i][j]==2:
            j-=1
        #move up
        elif dp[i][j]==3:
            i-=1
        else:
            print(i,j)
            break
    print(string)
    string = ''.join(string[::-1])
    return "YES" if string==b else "NO"




# if __name__ == '__main__':
q = int(input())
for q_itr in range(q):
    a = input()
    b = input()
    result = abbreviation(a, b)
    print(result)

# main()