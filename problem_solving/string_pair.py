from collections import Counter
number = [0]*101
number[1]=2
number[2]=1
number[3]=2
number[4]=2
number[5]=2
number[6]=1
number[7]=2
number[8]=2
number[9]=2
number[10]=1
number[11]=3
number[12]=2
number[13]=3
number[14]=4
number[15]=3
number[16]=3
number[17]=4
number[18]=4
number[19]=4
number[20]=1
number[30]=1
number[40]=1
number[50]=1
number[60]=1
number[70]=2
number[80]=2
number[90]=2
number[100]=2
for i in range(21,101):
    if i%10==0:
        continue
    else:
        d  = i//10
        r =  i%10
        number[i] = number[d*10]+number[r]
def findNPair(arr,count):
    counter = Counter(arr)
    arr = list(counter.keys())
    arr.sort()
    i =0
    j=len(arr)-1
    ans = 0
    while i<j:
        v= arr[i] + arr[j]
        if v==count:
            ans+= counter[arr[i]]*counter[arr[j]]
            i+=1
            j-=1
        elif v>count:
            j-=1
        else:
            i+=1
    return ans
#Driver code
# n = int(input())
# arr = list(map(int,input().split()))
n = 3
arr = [7,4,2]
count = 0
for x in arr:
    count += number[x]
# arr.sort()
print(count)
ans = findNPair(arr,count)

# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine
# 10 ten
# 11	eleven
# 12	twelve
# 13	thirteen
# 14	fourteen
# 15	fifteen
# 16	sixteen
# 17	seventeen
# 18	eighteen
# 19	nineteen
# 20	twenty
# 30	thirty
# 40	forty
# 50	fifty
# 60	sixty
# 70	seventy
# 80	eighty
# 90	ninety
# 100	 hundred