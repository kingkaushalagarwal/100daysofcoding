from testInput import input
from copy import deepcopy

def find(arr,i,visited,val,minn,dp):
    l = ['0']*402
    for j in range(len(visited)):
        if visited[j]==True:
            l[j]='1'
    string = ''.join(l)
    if string in dp:
        return

    if i==len(arr):
        minn[0] = min(minn[0],val)
        return
    ind = arr[i]
    if visited[ind]==False:
        visited[ind]=True
        find(arr,i+1,visited,val,minn,dp)
    else:
        for j in range(arr[i]-1,0,-1):
            if visited[j]==False:
                diff = arr[i] - j
                new_visited = deepcopy(visited)
                new_visited[j]=True
                find(arr,i+1,new_visited,val+diff,minn,dp)
        for j in range(arr[i]+1,402):
            if visited[j]==False:
                diff=j-arr[i]
                new_visited = deepcopy(visited)
                new_visited[j] = True
                find(arr, i + 1, new_visited, val + diff, minn,dp)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    visited =[False]*402
    minn = [9999999]
    dp ={}
    find(arr,0,visited,0,minn,dp)
    print(minn[0])