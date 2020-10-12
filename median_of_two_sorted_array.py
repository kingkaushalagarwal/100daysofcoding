def find(arr1,arr2):
    if len(arr1)==len(arr2)==2:
        return (max(arr1[0],arr2[0]) + min(arr1[1]+arr2[1]))//2

#median of two sorted array of same size
n =int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
