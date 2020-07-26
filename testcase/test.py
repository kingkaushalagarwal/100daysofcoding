from testInput import input
for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    stack=[];maxarea=0
    for i in range(len(arr)):
        x = arr[i]
        if len(stack)==0:
            stack.append(i)
        elif arr[ stack[-1] ]<=arr[i]:
            stack.append(i)
        else:
            while len(stack)!=0 and arr[stack[-1]]>arr[i]:
                height = arr[stack.pop()]  #top element of array
                if len(stack)==0:
                    length = i
                else:    
                    length = (i-stack[-1]-1)
                area = height*length
                maxarea= max(maxarea,area)
                # print(length, height, area, maxarea)

            stack.append(i)
        # print(stack)
    while len(stack)!=0:
        height = arr[stack.pop()]
        if len(stack)==0:
            length = i
        else:    
            length = (i-stack[-1]-1)
        area = height*length 
        maxarea= max(maxarea,area)
    print(maxarea)
"""
2
7
6 2 5 4 5 1 6
4
6 3 4 2
"""