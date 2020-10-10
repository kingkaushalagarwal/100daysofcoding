# from testInput import input
#for checking of power 2
def check(num):
    n = num
    if n==1:
        return True
    count =0
    while n>0:
        if n&1==1:
            count+=1
        n= n>>1
    if count>1:
        return True
    else:
        return False

def find(n):
    #if number is power of 2 than it is not possible to generate any such array
    if check(n)==False:
        return [-1]
    elif n == 5:
        return [2, 3, 1, 5, 4]
    elif n==3:
        return [2, 3, 1]
    elif n==1:
        return [1]
    else:
        arr =[2,3,1,5,4]
        i=6;flag= True
        while i<=n:
            if flag:
                arr.append(i)
                if (i+1)>n:
                    break
                arr.append(i+1)
                flag = False
            else:
                if (i+1)>n:
                    arr.append(i)
                    break
                else:
                    arr.append(i+1)
                    arr.append(i)
                    flag = True
            i+=2
        return arr
#for cross-verification function
def verify(arr):
    if arr==[-1]:
        return 0
    flag = True
    for  i in range(1,len(arr)):
        if arr[i-1]&arr[i]<=0:
            return 0
    return 1

#Driver Code
for _ in range(int(input())):
    n =int(input())
    arr = find(n)
    print(*arr)

