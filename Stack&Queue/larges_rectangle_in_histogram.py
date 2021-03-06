def justSmallLeft(arr):
    n = len(arr)
    ans = [0]*n
    stack =[]
    for  i in range(n):
        x = arr[i]
        if len(stack)==0 or arr[stack[-1]]<=arr[i]:
            stack.append(i)
        else:
            while len(stack)!=0 and arr[stack[-1]]>arr[i]:
                ind = stack.pop()
                ans[ind]=i
            stack.append(i)

    while len(stack)!=0:
        ind = stack.pop()
        ans[ind]=-1
    return ans
def justSmallRight(arr):
    n = len(arr)
    ans = [0]*n
    stack =[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0 or arr[stack[-1]]<=arr[i]:
            stack.append(i)
        else:
            while len(stack)!=0 and arr[stack[-1]]>arr[i]:
                ind = stack.pop()
                ans[ind]=i
            stack.append(i)
    while len(stack)!=0:
        ind = stack.pop()
        ans[ind]=-1
    return ans



def solve(A):
    n = len(A)
    left = justSmallLeft(A)
    right = justSmallRight(A)
    maxx = float('-inf')
    for i in range(len(A)):
        if left[i]==right[i]==-1:
            area= n * A[i]
        elif left[i]==-1:
            area = (n-right[i]-1)*A[i]
        elif right[i]==-1:
            area = left[i]*A[i]
        else:
            area = (left[i] - right[i] -1 )*A[i]
        maxx = max(maxx,area)
    return maxx
A = [2, 1, 5, 6, 2, 3]

A =[[0, 1, 1],
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 1, 1],
  [0, 1, 0]]
print(solve([0,1,1]))
# for i in range(len(A)):
#     print(solve(A[i]))
# ans = solve(A)
# print(ans)