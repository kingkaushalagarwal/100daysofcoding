from testInput import input
def preProcessing(arrary):
    n = len(array)
    new_array = []
    for i in range(n):
        num = array[i]
        bits = [0] * 32
        k = 0
        while num > 0:
            if num & 1:
                bits[k] = 1
            num = num >> 1
            k += 1
        new_array.append(bits)
    for i in range(1, n):
        for j in range(32):
            new_array[i][j] += new_array[i - 1][j]
    return new_array


def optimize(new_array, l, r):
    minn = 10 ** 30
    for k in range(32):
        if (l - 1) >= 0:
            num = new_array[r][k] - new_array[l - 1][k]
        else:
            num = new_array[r][k]
        required = ((r - l + 1) - num) * (2 ** k)
        minn = min(minn, required)
    print(minn)


def bruteForce(array, l, r):
    minn = r - l + 1
    print(array, l, r,minn)


    for i in range(32):
        count = 0
        for j in range(l, r + 1):
            if array[j] & (1 << i) == 0:
                count += 1
        minn = min(minn, count * (2 ** i))

    print(minn)


# Driver class
n = int(input())
array = list(map(int, input().split()))
Q = int(input())
# new_array = preProcessing(array)
for i in range(Q):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    if l > r:
        l, r = r, l
    if l == r:
        if array[l] != 0:
            print(0)
        else:
            print(1)
        continue
    # optimize(new_array,l,r)
    bruteForce(array, l, r)


