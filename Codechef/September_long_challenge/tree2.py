from testInput import input
for _ in range(int(input())):
    n = int(input())
    print(len(set(map(int, input().split()))))
