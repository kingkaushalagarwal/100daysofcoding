def find(arr,i,j,string):
    #last element of array
    if i==(len(arr)-1):

    temp =[]
    for k in range(j,len(arr[0])):
        ch1 = arr[i][j]
        ch2 = arr[i+1][j]
        if ch1<ch2:
            temp.append(ch1)


for _ in range(int(input())):
    n,m = map(int,input().split())
    arr =[]
    for i in range(n):
        arr.append(input())
    string = []
    string.append(arr[0][0])


