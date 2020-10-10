from copy import deepcopy
from collections import deque
# from testInput import input
def find(string):
    prefix = [0] * n
    cost = 0
    prev = 'L'
    for i in range(n):
        if string[i] == 'W':
            if prev == 'W':
                cost += 2
                prefix[i] = cost
            else:
                cost += 1
                prefix[i] = cost
        else:
            prefix[i] = cost
        prev = string[i]

    queue = deque()
    s = 0
    max_summ = 0

    for i in range(len(string)):
        if string[i] == 'L':
            queue.append(i)
            if len(queue) == (k + 1):
                e = queue[-1]
                length = e - s
                cost = length * 2 - 1
                if s - 1 >= 0:
                    cost += prefix[s - 1]
                if (e - 1) >= 0:
                    cost += prefix[-1] - prefix[e - 1]

                max_summ = max(max_summ, cost)
                s = queue.popleft() + 1
    length = (n - s)
    cost = length * 2 - 1
    if (s - 1) >= 0:
        cost += prefix[s - 1]

    max_summ = max(max_summ, cost)
    return max_summ


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
        string1= deepcopy(string)
        string2= deepcopy(string[::-1])
        ans= max(find(string1),find(string2))
    print(ans)
    # if t==0:
    #     print(ans,end="")
    # else:
    #     print("\n"+str(ans),end="")
