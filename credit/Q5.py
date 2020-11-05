from testInput import input
b,bankers = input().split()
p,participants = input().split()
b,p = int(b),int(p)
bankers = bankers.split(',')
participants = participants.split(',')
barray = [set() for i in range(b)]
parray =[set() for i in range(p)]
for i in range(len(bankers)):
    l = bankers[i].split('&')
    for x in l:
        x= int(x)
        barray[i].add(x)
        parray[x-1].add(i + 1)
for i in range(len(participants)):
    l = participants[i].split('&')
    for x in l:
        x = int(x)
        parray[i].add(x)
        barray[x-1].add(i+1)
print(max(max([len(x) for x in barray]),max([len(x) for x in parray])))