# 0 1 2 3 4 5 6 7 8 9 10
# 0 1 5 N N 2 9 N 8 6 10
"""
if number conatins 3,4 7 then they are not good
number is good only if it conatins one of these digits - 2,5,6,9
"""


class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for i in range(1, N + 1):
            flag1 = False
            flag2 = True
            while i > 0:
                if i % 10 in [2, 5, 6, 9]:
                    flag1 = True
                    break
                if i % 10 in [3, 4, 7]:
                    flag2 = False
                    break
                i = i // 10
            if flag1 == True and flag2 == True:
                count += 1
            print(i,count)
            # else:
            #     print(i,count)
        return count
N = int(input())
ans = Solution().rotatedDigits(N)
print(ans)