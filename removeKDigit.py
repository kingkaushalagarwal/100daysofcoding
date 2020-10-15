class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[]
        for digit in num:
            if k>0 and len(stack)>0 and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        if k>0:
            stack =stack[:-k]
        string = ''.join(stack).lstrip('0')
        if string=='':
            string = '0'
        return string
string = input()
k = int(input())
ans = Solution().removeKdigits(string,k)
print(ans)