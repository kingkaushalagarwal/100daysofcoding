class Solution:

    def minInsertions(self, s: str) -> int:
        right = 0
        l = [];
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                if right == 1:
                    l.append(1)
                    right = 0
                    ans += 1
                l.append(0)
            elif s[i] == ')':
                right += 1
                if right % 2 == 0:
                    l.append(1)
                    right = 0
        if right == 1:
            l.append(1)
            ans+=1
        flag = False
        count1 = 0;
        count0 = 0
        print(l,ans)
        stack =[]
        for i in range(len(l)):
            if l[i] == 1 and flag == False:
                ans += 1
            elif l[i]==0:
                flag = True
                stack.append(0)
            elif l[i]==1:
                if len(stack)==0:
                    ans+=1
                else:
                    stack.pop()
        ans += len(stack)*2


        return ans
s = "))(()()))()))))))()())()(())()))))()())(()())))()("
# Output: 12
ans  =Solution().minInsertions(s)
print(ans)

