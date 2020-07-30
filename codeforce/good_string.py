# from testInput import input
for _ in range(int(input())):
    string = input().strip()
    count =[0]*10
    for x in string:
        count[int(x)]+=1
    maxx =-1
    for i in range(10):
        for j in range(i+1,10):
            n=i;m=j
            c=0
            flag = True
            for k in range(len(string)):
                if flag==True:
                    if string[k]==str(n):
                        c+=1
                        flag = False
                else:
                    if string[k]==str(m):
                        c+=1
                        flag = True
            if c%2==0:
                maxx =max(maxx,c)
    print(len(string)-max(maxx,max(count)))