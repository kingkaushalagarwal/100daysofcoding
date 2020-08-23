from testInput import input
for t in range(int(input())):
    n, a, b, c = map(int, input().split())
    print(n,a,b,c)
    d1 = a - c
    d2 = b - c
    if (d1 + d2 + c) > n or c > a or c > b:
        print("Case #", t + 1, ": ", "IMPOSSIBLE", sep="")
    else:
        ans = [0] * n
        middle = n - c + 1
        if a==c or b == c:
            k = 1
            for i in range(n-1,-1,-1):
                # print(i,n-c,ans)
                if n-c<=i:
                    ans[i] = middle
                else:
                    ans[i]=k
                    k +=1
            if a==c:
                ans = ans[::-1]
        else:
            d=d1
            print(middle,d)
            for i in range(d1,c):
                if i<d1:
                    ans [i]=d
                    d-=1
                elif i<(d1+c):
                    ans[i]=middle
            # for i in range(d1+c,n):
            #     ans[i]=i
        print("Case #",t+1,": ",sep="",end="")
        print(*ans)

