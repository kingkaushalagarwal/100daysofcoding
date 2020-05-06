#Codechef may long challenge problem 2
#Isolation centers
from collections import Counter
for _ in range(int(input())):
    N,Q = map(int,input().split())
    s = input()
    counter = Counter (s)
    for i in range(Q):
        c = int(input())
        count = 0 
        for v in counter.values():
            if v>c :
                count += v-c
        print(count)        
        