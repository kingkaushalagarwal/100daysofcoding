#giving wrong answer
from testInput import input
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    # print(type(counter1.keys()))
    keys1 = sorted(list(counter1.keys()))
    keys2 = sorted(list(counter2.keys()))
    diffKey1 = [];diffKey2=[]
    flag = False
    for x in keys1:
        value1 = counter1[x]
        if x in counter2:
            value2 = counter2[x]
            if value1>value2:
                if (value1 - value2)%2 == 1:
                    flag = True
                    break
                else:
                    diff = (value1-value2)//2
                    diffKey1.append([x,diff])
        else:
            if value1%2==1:
                flag = True
                break
            diffKey1.append([x,value1//2])
    if flag:
        print(-1)
        continue
    for x in keys2:
        value1 = counter2[x]
        if x in counter2:
            value2 = counter1[x]
            if value1>value2:
                if (value1-value2)%2==1:
                    flag = True
                    break
                else:
                    diff = (value1-value2)//2
                    diffKey2.append([x,diff])
        else:
            if value1%2==1:
                flag = True
                break
            diffKey2.append([x,value1//2])
    if flag:
        print(-1)
        continue
    # print(diffKey1)
    # print(diffKey2)
    i=0;j=len(diffKey2)-1
    cost=0
    while(i<len(diffKey1) and j>=0):
        cost+=min(diffKey1[i][0],diffKey2[j][0])
        diffKey1[i][1]-=1
        diffKey2[j][1]-=1
        if diffKey1[i][1]==0:
            i+=1
        if diffKey2[j][1]==0:
            j-=1
    print(cost)

