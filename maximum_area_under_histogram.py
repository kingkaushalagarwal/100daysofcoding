# from testInput import input
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    stack = [];
    maxarea = 0
    for i in range(len(arr)):
        x = arr[i]
        if len(stack) == 0 or arr[stack[-1]] <= arr[i]:
            stack.append(i)
        else:
            while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                height = arr[stack.pop()]  # top element of array
                if len(stack) == 0:
                    length = i
                else:
                    length = (i - stack[-1] - 1)
                area = height * length
                maxarea = max(maxarea, area)
            stack.append(i)

    while len(stack) != 0:
        height = arr[stack.pop()]
        if len(stack) == 0:
            length = n
        else:
            length = (n - stack[-1] - 1)
        area = height * length
        maxarea = max(maxarea, area)
    print(maxarea)
