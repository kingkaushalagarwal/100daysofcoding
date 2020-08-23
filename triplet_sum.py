def dailyTemperatures( T):
    ans = [-1] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i# from testInput import i# from testInput import input
from collections import Counternput
from collections import Counter
        stack.append(i)

    return ans
T =[ 5,4,3,2,1 ]
ans = dailyTemperatures(T)/
print(ans)