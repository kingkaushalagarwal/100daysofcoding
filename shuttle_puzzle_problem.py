#InterviewBit
#Shuttle puzzle problem
#backtracking
import sys
class Solution:
    # @param A : integer
    # @return a list of strings
    def check(self,l):
        length = len(l)//2
        for i in range(length):
            if l[i]!='B':
                return False
        if l[length]!='H':
            return False
        return True

    def solveUtil(self,l,i,n,count,array,minn,ans):
        if self.check(l):
            if minn[0]>count:
                minn[0] = count
                ans[0]=array
            return True
        if count>minn[0]:
            return
        if i-1>=0 and l[i-1]=='W':
            l[i-1],l[i]= l[i],l[i-1]
            self.solveUtil(l,i-1,n,count+1,array +["".join(l)],minn,ans)
            l[i-1],l[i]= l[i],l[i-1]
        if i+1<n and l[i+1]=='B':
            l[i],l[i+1]= l[i+1],l[i]
            self.solveUtil(l,i+1,n,count+1,array +["".join(l)],minn,ans)
            l[i],l[i+1]= l[i+1],l[i]
        if i+2<n and l[i+2]!=l[i+1] and l[i+2]=='B':
            l[i],l[i+2] = l[i+2],l[i]
            self.solveUtil(l,i+2,n,count+1,array +["".join(l)],minn,ans)
            l[i],l[i+2] = l[i+2],l[i]

        if i-2>=0 and l[i-2]!=l[i-1] and l[i-2]=='W':
            l[i-2],l[i] = l[i],l[i-2]
            self.solveUtil(l,i-2,n,count+1,array +["".join(l)],minn,ans)
            l[i-2],l[i] = l[i],l[i-2]


    def solve(self, A):
        l = ['W']*A + ['H'] + ['B']*A
        count = 0
        array =["".join(l)]
        minn = [300]
        n = len(l)
        ans =[0]
        self.solveUtil(l,A,n,count,array,minn,ans)
        return ans[0]#Driver Code
