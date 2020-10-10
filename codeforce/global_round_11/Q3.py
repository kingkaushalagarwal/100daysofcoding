from copy import deepcopy
# from testInput import input
def findCost(string):
    prev = 'L'
    cost = 0
    for i in range(len(string)):
        if string[i] == 'W':
            if prev == 'W':
                cost += 2
            else:
                cost += 1
        prev = string[i]
    return cost


def find(string,k):
    n = len(string)
    for i in range(1,len(string)):
        if k>0 and string[i-1]=='W' and string[i]=='L':
            string[i]='W'
            k-=1
    for i in range(n-2 ,-1,-1):
        if k>0 and string[i+1]=='W' and string[i]=='L':
            string[i]='W'
            k-=1
    for i in range( len(string)):
        if k > 0 and  string[i] == 'L':
            string[i] = 'W'
            k -= 1
    return findCost(string)



for t in range(int(input())):
    n,k = map(int,input().split())
    string = list(input())
    num  = string.count('L')
    if len(string)==0:
        ans = 0
    elif k==0:
        prev= 'L'
        cost = 0
        for i in range(n):
            if string[i]=='W':
                if prev=='W':
                    cost+=2
                else:
                    cost+=1
            prev = string[i]
        ans = cost
    else:
        cost = 0
        for i in range(1,n-1):
            if k>0 and string[i-1]=='W' and string[i+1]=='W' and string[i]=='L':
                string[i]='W'
                k-=1
        string1 = deepcopy(string)
        string = string[::-1]
        string2 = deepcopy(string)
        # print("string1",string1)
        # print("string2",string2)
        # print("K ",k)
        ans = max(find(string1,k) ,find(string2,k))
    print(ans)