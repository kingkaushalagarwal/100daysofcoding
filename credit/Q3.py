from testInput import input
def find(prices, profit):
    d = {}
    for i in range(len(prices)):
        selling_price = prices[i]
        buying_price = selling_price - profit
        if buying_price in d:
            return str(d[buying_price]) + " " + str(i + 1)
        else:
            d[selling_price] = i + 1

    return "-1"


def find_min_days(prices, profit):
    ans = []
    for x in profit:
        ans.append(find(prices, x))
    return ','.join(ans)


n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices, profit)
# Do not remove below line
print(answer)
# Do not print anything after this line