#solution is based on this blog
# from testInput import input
#local maxima and local minima solution for pokeman easy question
#local maxima and local minima solution for pokeman hard question
def makeChange(arr,i,sign,ans):
    if i==0 or i==(len(arr)-1):
        return
    #case of maxima
    if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
        ans[0] += sign*arr[i]
    #case of minima
    if arr[i-1]>arr[i] and arr[i+1]>arr[i]:
        ans[0] -= sign*arr[i]

def performChange(arr,sign,l,r,ans):
    if (l==r):
        return
    if (l+1==r):
        makeChange(arr,l-1,sign,ans)
        makeChange(arr,l,sign,ans)
        makeChange(arr, r , sign,ans)
        makeChange(arr, r+1, sign,ans)
    else:
        makeChange(arr, l - 1, sign,ans)
        makeChange(arr, l, sign,ans)
        makeChange(arr, l+1, sign,ans)
        if (l+2!=r):
            makeChange(arr,r-1,sign,ans)
        makeChange(arr, r, sign,ans)
        makeChange(arr, r + 1, sign,ans)

def pokemanHard(arr,q):
    arr = [-1]+arr + [-1]
    count =0
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            count += arr[i]
        if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
            count -= arr[i]
    ans =[count]
    final_ans =[count]
    # print(arr)
    for i in range(q):
        l,r = map(int,input().split())
        #updating answer
        if (l!=r):
            performChange(arr,-1,l,r,ans)
            arr[l],arr[r]=arr[r],arr[l]
            performChange(arr,1,l,r,ans)
        final_ans.append(ans[0])
    for i in range(len(final_ans)):
        print(final_ans[i])
    return

#Driver Code
for _ in range(int(input())):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    pokemanHard(arr,q)