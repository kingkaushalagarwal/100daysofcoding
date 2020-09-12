def justGreaterRight(arr):
    n = len(arr)
    ans = [0] * n
    stack = []
    for i in range(n):
        x = arr[i]
        if len(stack) == 0 or arr[stack[-1]] >= arr[i]:
            stack.append(i)
        else:
            while len(stack) != 0 and arr[stack[-1]] < arr[i]:
                ind = stack.pop()
                ans[ind] = i
            stack.append(i)
    while len(stack) != 0:
        ind = stack.pop()
        ans[ind] = -1
    return ans


def justGreaterLeft(arr):
    n = len(arr)
    ans = [0] * n
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        if len(stack) == 0 or arr[stack[-1]] >= arr[i]:
            stack.append(i)
        else:
            while len(stack) != 0 and arr[stack[-1]] < arr[i]:
                ind = stack.pop()
                ans[ind] = i
            stack.append(i)
    while len(stack) != 0:
        ind = stack.pop()
        ans[ind] = -1
    return ans
def solve(arr):
    left = justGreaterLeft(arr)
    right = justGreaterRight(arr)
    summ =0
    n = len(arr)
    for i in range(len(arr)):
        if left[i]==-1 and right[i] ==-1:
            summ += n
        elif right[i]==-1:
            summ += n - (left[i]+1)
        elif left[i]==-1:
            summ+= right[i]
        else:
            summ += right[i] - left[i] -1
    return summ

def calculateTotalRegion(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return 1
    else:
        return solve(arr)
# arr =[1,2,1]
# ans = calculateTotalRegion(arr)
# print(ans)