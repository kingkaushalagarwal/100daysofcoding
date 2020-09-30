for _ in range(int(input())):
    a = int(input())
    total_sum = ((a-1)*(a))//2
    m =10**9+7
    for i in range(2,a):
        f = (i-1)*a+i
        l = i*a-1
        summ = ((a-i)*(f+l))//2
        total_sum = (total_sum + summ)%m
    print(total_sum)