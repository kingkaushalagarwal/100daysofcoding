n = int(input())
queue = list(input())
# queue = list("--AB--AB---A--")
# n = len(queue)
maxx = 100005
A = [maxx]*n
B = [maxx]*n
prev = -1
for i in range(n):
    if queue[i]=='B':
        prev = i
    elif queue[i]=='A':
        prev=-1
    elif prev!=-1 and queue[i]=='-':
        B[i] = i - prev
prev = -1
for i in range(n-1,-1,-1):
    if queue[i]=='A':
        prev = i
    elif queue[i]=='B':
        prev=-1
    elif prev!=-1 and queue[i]=='-':
        A[i] = prev - i
ans = [0]*n
for i in range(n):
    if queue[i]=='A':
        ans [i]='A'
    elif queue[i]=='B':
        ans[i]='B'
    else:
        if A[i]==B[i]:
            continue
        if A[i]<B[i]:
            ans[i]='A'
        elif B[i]<A[i]:
            ans[i]='B'
countA =0
countB= 0
for i in range(n):
    if ans[i]=='A':
        countA+=1
    elif ans[i]=='B':
        countB+=1
if countA>countB:
    print('A')
elif countB>countA:
    print('B')
else:
    print("Coalition government")
