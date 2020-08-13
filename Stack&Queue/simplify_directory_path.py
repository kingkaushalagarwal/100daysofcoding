class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        stack = []
        l=[]
        for x in A:
            if x=='/':
                if len(l)==0:
                    continue
                else:
                    string = ''.join(l)
                    if string=='.':
                        pass
                    elif string=='..':
                        if stack:
                            stack.pop()
                    else:
                        # print(string)
                        stack.append(string)
                    l=[]
            else:
                l.append(x)
        if len(l)!=0:
            string = ''.join(l)
            if string == '.':
                pass
            elif string == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(string)
        ans ='/'
        ans = ans+  '/'.join(stack)

        return ans


A =["/home/","/a/./b/../../c/","/a/..","/a/../","/../../../../../a","/a/./b/./c/./d/","/a/../.././../../.","/a//b//c//////d"]
B =["/home","/c","/","/","/a",'/a/b/c/d',"/","/a/b/c/d"]

for i in range(len(A)):
    ans  = Solution().simplifyPath(A[i])
    print(A[i]+"   "+ans+"    "+B[i])