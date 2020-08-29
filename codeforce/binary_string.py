# from testInput import input
for _ in range(int(input())):
    string1 = input()
    x = int(input())

    n = len(string1)
    # print("length: ",n,string1)
    dp = [0]*n
    if len(string1)==1:
        if string1[0]=='0':
            print(0)
        elif string1[0]=='1':
            print(-1)
    else:
        string = [int(x) for x in string1 ]
        ans = [-1]*len(string)
        flag = True
        for i in range(len(string)):
            p1 = i-x
            p2 = i+x
            if (p1 >= 0 and p1 < n) and not (p2>=0 and p2<n):
                if ans[p1]==-1:
                    if string[i]==1:
                        ans[p1]=1
                        dp[i]=1
                    else:
                        ans[p1]=0
                else:
                    if ans[p1]!=string[i] :
                        if dp[p1]==2:
                            dp[p1]-=1
                        else:
                            flag = False
                            break

            elif (p2>=0 and p2<n) and not(p1 >= 0 and p1 < n):
                if ans[p2]==-1:
                    if string[i]==1:
                        ans[p2]=1
                        dp[i]=1
                    else:
                        ans[p2]=0
                else:
                    if ans[p2]!=string[i]:
                        if dp[p2] == 2:
                            dp[p2] -= 1
                        else:
                            flag = False
                            break
            elif (p2>=0 and p2<n) and not(p1 >= 0 and p1 < n):
               if string[i]==1:
                   if ans[p1]==-1 and ans[p2]==-1:
                       ans[p1]=1
                       ans[p2]=1
                       dp[i] =2
                   elif ans[p1]!=string[i] 


        if flag==False:
            print(-1)
        else:
            print(''.join([str(x) for x in ans]))
