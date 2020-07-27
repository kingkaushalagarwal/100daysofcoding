for _ in range(int(input())):
    A, B = input().split()
    n = len(A);
    m = len(B)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    move = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if B[i - 1] == A[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                move[i][j]= 3
            else:
                if dp[i-1][j]>dp[i][j-1]:
                    dp[i][j]=dp[i-1][j]
                    #up
                    move[i][j]=2
                else:
                    dp[i][j] =  dp[i][j - 1]
                    #horizontal one
                    move[i][j]=1
    l=[]
    i=m;j=n
    while i>=0 and j>=0:
         if i==0 and j==0:
             break
         if move[i][j]==3:
            l.append(A[j-1])  #or l.append(B[i-1])
            i-=1;j-=1
         elif move[i][j]==2:       #up
            l.append(B[i-1])
            i-=1
         elif move[i][j]==1: #horizontal
            l.append(A[j-1])
            j-=1
         else:
             while i==0 and j!=0:
                 l.append(A[j-1])
                 j-=1
             while j==0 and i!=0:
                 l.append(B[i-1])
                 i-=1
    print(''.join(l[::-1]))

    lcs = dp[-1][-1]

    print(n + m - lcs)