# from testInput import input
def find(arr,i,l,answer):
    if i==len(arr[0]):
        for i in range(len(answer)):
            answer[i]=l[i]
        return True

    for  k in range(3):
        if len(l)==0 :
            if find(arr,i+1,l+[arr[k][i]],answer):
                return True
        elif i<len(arr[0])-1 and  l[-1] != arr[k][i]:
            if find(arr, i + 1, l + [arr[k][i]], answer):
                return True
        elif i == len(arr[0]) - 1 and l[0] != arr[k][i] and l[-1]!=arr[k][i]:
            if find(arr, i + 1, l + [arr[k][i]], answer):
                return True

    return False
for _ in range(int(input())):
    n = int(input())
    arr =[]
    arr.append(list(map(int,input().split())))
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
    answer = [0]*n
    find(arr,0,[],answer)
    print(*answer)