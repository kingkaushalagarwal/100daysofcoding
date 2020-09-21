from testInput import input
def method1(l):
    addition = 0
    available = [True]*n
    for x in l:
        addition = addition + x[1]
    summ =0
    for i in range(n-1):
        minn = None
        ind =-1
        for j in range(n):
            if available[j] == True:
                num = l[j][0]*(addition - l[j][1])
                if minn == None:
                    minn = num
                    ind = j
                elif minn>num:
                    minn = num
                    ind = j
                elif minn==num:
                    if l[ind][0]*l[ind][1]<l[j][0]*l[j][1]:
                        ind = j



        available[ind]= False
        summ += minn
        addition = addition - l[ind][1]
    return summ
def method2(l):
    nl =[]
    n  = len(l)
    for i in range(n):
        nl.append([l[0]*l[1],i])
    nl.sort(reverse = True)
    nll =[]
    for i in range(n):
        nll.append(l[nl[i][1]])
    print(nll)


for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(3):
        na = list(map(int, input().split()))
        arr.append(na)
    l = []
    for i in range(n):
        num1 = arr[0][i]
        num2 = arr[1][i] * arr[2][i]
        l.append([num1, num2])

    print(method1(l))




    # l.sort()
    # prefix1 = creating_Prefix_array(l)
    # print(l)
    # print(prefix1)
    # summ1 = 0
    # for i in range(n - 1):
    #     summ1 += l[i][0] * prefix1[i + 1]
    # l.sort(key=lambda x: x[1],reverse=True)
    #
    # prefix2 = creating_Prefix_array(l)
    # print(l)
    # print(prefix2)
    # summ2 = 0
    # for i in range(n - 1):
    #     summ2 += l[i][0] * prefix2[i + 1]
    # print(min(summ1, summ2))
