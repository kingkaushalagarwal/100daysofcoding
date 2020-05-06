#may long challenge div 2 codechef
#cronavirus spread
# 1 2 5 6 7
# 1 1 1 3
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(len(arr)-1):
        arr[i] =arr[i+1] - arr[i]
    best = 1; worst = len(arr)
    count =0
    for i in range(len(arr)-1):    
        if arr[i]<=2:
            count+= 1
        else:
            count +=1
            best = max(best,count)
            worst = min(worst,count)
            count = 0 
    count +=1        
    best = max(best,count)
    worst = min(worst,count)
    count = 0
    print(worst,best)
        