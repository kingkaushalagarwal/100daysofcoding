n = 10
combination = [[1],[1,1]]
for i in range(2,11):
    combination.append([0]*(i+1))
    combination[i][0]=1
    combination[i][-1] = 1
    for j in range(1,i):
        combination[i][j] = combination[i-1][j-1] + combination[i-1][j]
for i in range(len(combination)):
    print(combination[i])
for i in range(len(combination)):
    x = combination[i]
    for j  in range(1,len(x)):
        x[j]+=x[j-1]
for i in range(len(combination)):
    print(combination[i])

