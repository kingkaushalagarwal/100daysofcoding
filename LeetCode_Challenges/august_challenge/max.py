class Solution:
    def canConvertString(self, s: str, t: str, k: int) :

        if len(s) != len(t):
            return False
        n = len(s)
        diff = [0] * n
        for i in range(n):
            ch1 = ord(s[i])
            ch2 = ord(t[i])
            if ch1 < ch2:
                diff[i] = ch2 - ch1
            elif ch1 > ch2:
                diff[i] = 26 - (ch1 - ch2 )
        print(diff)
        if max(diff) > k:
            return False
        number = [0] * 26
        for i in range(n):
            # print(number)
            num = diff[i]
            if num > 0:
                if number[num] == 0:
                    number[num] = 1
                else:
                    if (number[num] * 26 + num) <= k:
                        number[num] += 1
                    else:
                        return False
        print(number)
        return True
s = "iqssxdlb"
t ="dyuqrwyr"
k =40
# k = 27
ans = Solution().canConvertString(s,t,k)
print(ans)