def leftSmaller(arr):
    n = len(arr)
    stack=[]
    smaller = [-1]*n
    for i in range(n):
        if len(stack)==0 or arr[stack[-1]]<=arr[i]:
            stack.append(i)
        else:
            while stack and arr[stack[-1]]>arr[i]:
                ind = stack.pop()
                smaller[ind]=i
            stack.append(i)
    return smaller
def rightSmaller(arr):
    n= len(arr)
    stack=[]
    smaller=[-1]*n
    for i in range(n-1,-1,-1):
        if len(stack)==0 or arr[stack[-1]]<=arr[i]:
            stack.append(i)
        else:
            while stack and arr[stack[-1]]>arr[i]:
                ind = stack.pop()
                smaller[ind]=i
            stack.append(i)
    return smaller


def find(arr):
    left = leftSmaller(arr)
    right = rightSmaller(arr)
    n = len(arr)
    summ = sum(arr)
    prefixSum = [0]*n
    prev =0
    for i in range(n):
        prefixSum[i]=prev + arr[i]
        prev=  prefixSum[i]
    maxx = float('-inf')
    for i in range(n):
        if left[i]==-1 and right[i]==-1:
            width = prefixSum[n-1]
        elif left[i]==-1:
            ind = right[i]
            width = prefixSum[n-1] - prefixSum[ind]
        elif right[i]==-1:
            ind = left[i]-1
            width = prefixSum[ind]
        else:
            ind1 = left[i]-1
            ind2 = right[i]
            width= prefixSum[ind1]-prefixSum[ind2]
        value = width * arr[i]
        maxx = max(maxx, value)
    return maxx

# arr = list(map(int,input().split()))
arr = [3,1,6,4,5,2]
print(find(arr))