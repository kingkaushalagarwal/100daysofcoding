import math
import sys

# from testInput import input
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b // gcd(a, b)


def power(num, x, m):
    if x == 0:
        return 1
    if x == 1:
        return num % m
    if x & 1 == 0:  # even number
        return power((num % m * num % m) % m, x // 2, m)
    else:
        return (num % m * power((num % m * num % m) % m, (x - 1) // 2, m)) % m


def check(num1, num2, k):
    i = 2
    while (i < int(math.sqrt(max(num1, num2))) + 1):
        count1 = 0
        count2 = 0
        while num1 % i == 0:
            num1 = num1 // i
            count1 += 1
        while num2 % i == 0:
            num2 = num2 // i
            count2 += 1
        if count1 * k < count2:
            return False
        i += 1
    if num1 != num2:
        return False
    return True


def LCM(arr, n):
    # Find the maximum value in arr[]
    max_num = 0;
    for i in range(n):
        if (max_num < arr[i]):
            max_num = arr[i];

            # Initialize result
    res = 1;

    # Find all factors that are present
    # in two or more array elements.
    x = 2;  # Current factor.
    while (x <= max_num):

        # To store indexes of all array
        # elements that are divisible by x.
        indexes = [];
        for j in range(n):
            if (arr[j] % x == 0):
                indexes.append(j);

                # If there are 2 or more array
        # elements that are divisible by x.
        if (len(indexes) >= 2):

            # Reduce all array elements
            # divisible by x.
            for j in range(len(indexes)):
                arr[indexes[j]] = int(arr[indexes[j]] / x);

            res = res * x;
        else:
            x += 1;

            # Then multiply all reduced
    # array elements
    for i in range(n):
        res = res * arr[i];

    return res;


# Driver Code
for _ in range(int(sys.stdin.readline())):
    n, m, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arrayLcm = 1
    flag = False
    # for i in range(len(arr)):
    #     arrayLcm = lcm(arrayLcm,arr[i])
    arrayLcm = LCM(arr, n)
    if arrayLcm % m == 0:
        print(0)
    elif check(arrayLcm, m, k):
        print(0)
    else:
        print(power(arrayLcm, k, m))

# 1
# 5 20 3
# 17 2 9 4 12
