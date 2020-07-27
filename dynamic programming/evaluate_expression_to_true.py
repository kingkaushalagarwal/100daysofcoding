A = input()
m = len(A)
# n = m//2
T= [[0]*n for i in range(n)]
F = [ [0]*n for i in range(n)]
for l in range(3,n+1):
    for i in range(n-l+1):
        j = i+l-1
        for k in range(i+1)