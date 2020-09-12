from testInput import input
def getShiftedString(s,l,r):
    if len(s)==0:
        return ""
    if l==r:
        return s
    n = len(s)
    if l>r:
        l = l-r
        l = l%n
        if l==0:
            return s
        else:
            return s[l:]+s[:l]
    else:
        r = r-l
        r = r%n
        if r==0:
            return s
        else:
            return s[-r:]+s[:-r]
# # while(True):
# for i in range(int(input())):
#     s = input()
#     l,r = map(int,input().split())
#     ans = getShiftedString(s,l,r)
#     print(s,l,r)
#     print(ans)