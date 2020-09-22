from testInput import input
from math import log
def find(arr, n):
    max_element = max(arr)
    max_bit = int(log(max_element, 2)) + 1
    ans = 0
    total_subarray = (n * (n + 1)) // 2
    print(arr,total_subarray)
    for i in range(max_bit):
        vector = []
        # find index of those element whose ith bit is not set
        for j in range(n):
            if (arr[j] & (1 << i)==0):
                vector.append(j)

        if len(vector) == 0:
            ans += total_subarray * (2 ** i)
        else:
            not_set_subarray = 0  # number of subarrays in which ith bit is not set
            c = 1
            for k in range(1, len(vector)):
                if vector[k] - vector[k - 1] == 1:
                    c += 1
                else:
                    not_set_subarray += (c * (c + 1)) // 2
                    c = 1
            not_set_subarray += (c * (c + 1)) // 2
            if len(vector) == 1:
                not_set_subarray = 1
            value= (total_subarray - not_set_subarray) * (2 ** i)
            ans+=value
            print(i,vector,value)
    return ans


# Driver Code
n = int(input())
arr = list(map(int, input().split()))
if n == 0:
    print(0)
elif n == 1:
    print(arr[0])
else:
    print(find(arr, n))