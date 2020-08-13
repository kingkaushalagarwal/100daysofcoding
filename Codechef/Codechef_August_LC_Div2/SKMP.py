from testInput import input
for _ in range(int(input())):
    S = input()
    P = input()
    char =[0]*26
    for x in S:
        x = ord(x) - 97
        char[x]+=1
    for i in range(len(P)):
        x  = ord(P[i])-97
        char[x]-=1
    flag = False
    for i in range(len(P)):
        x = ord(P[i]) - 97
        if i==0:
            num =x
        elif x==num:
            continue
        elif num<x:
            break
        elif num>x:
            flag = True
            False

    # print(S,P)
    for i in range(26):
        # if char[i]>0:
            if i==num:
                if flag==True:
                    print(P,end="")
                    print(chr(i+97)*char[i],end="")
                else:
                    print( chr(i + 97) * char[i], end="")
                    print(P, end="")
            else:
                print(chr(i + 97) * char[i], end="")

    print()

# aaakaeekmnnry
# abohotypsu
# aabadawyehhorst