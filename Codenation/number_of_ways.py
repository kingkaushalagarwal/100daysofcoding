from testInput import input
# Complete the solve function below.
def find(a,b,c,i,j,k,flag1,flag2):
    if k==len(c):
        if flag1 and flag2:
            return 1
        return 0
    if i>=len(a) and j>=len(b):
        return 0
    count =0
    if i < len(a) and a[i] == c[k] and j<len(b) and b[j]==c[k]:
        count += find(a, b, c, i + 1, j, k + 1,True,flag2)
        count += find(a ,b ,c, i, j+1, k+1,flag1,True)
        count += find(a, b, c, i + 1, j + 1, k,flag1,flag2)

    elif i<len(a) and a[i]==c[k]:
        count += find(a,b,c,i+1,j,k+1,True,flag2)
        count += find(a, b, c, i + 1, j, k,flag1,flag2)

    elif j<len(b) and b[j]==c[k]:
        count += find(a,b,c,i,j+1,k+1,flag1,True)
        count += find(a, b, c, i, j + 1, k,flag1,flag2)
    else:
        if j<len(b):
            count += find(a,b,c,i,j+1,k,flag1,flag2)
        if i<len(a):
            count += find(a, b, c, i+1, j , k,flag1,flag2)
        if i<len(a) and j<len(b):
            count -= find(a,b,c,i+1,j+1,k,flag1,flag2)
    return count


def solve(a, b, c):
    return find(a,b,c,0,0,0,False,False)

if __name__ == '__main__':
    abc = input().rstrip().split()

    a = abc[0]

    b = abc[1]

    c = abc[2]
    print(a,b,c)

    result = solve(a, b, c)
    print(result)