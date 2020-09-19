from itertools import combinations
class Solution:
    #using itertools library
    def combinationSum3(self, k: int, n: int):
        arr =[1,2,3,4,5,6,7,8,9]
        combi = combinations(arr,k)
        ans = []
        for x in combi:
            if sum(x)==n:
                ans.append(list(x))
        return ans

    #without using itertools
    def findCombi(self,i,l):

        if i==9:
            if len(l)==self.k:
                if sum(l)==self.n:
                    self.combi.append(l)
            return
        self.findCombi(i+1,l+[self.arr[i]])
        self.findCombi(i+1,l)

    def combinationSum4(self,k,n):
        self.arr = list(range(1,10))
        self.k =k
        self.combi = []
        self.n = n
        self.findCombi(0,[])
        return self.combi

k,n = map(int,input().split())
ans = Solution().combinationSum4(k,n)
print(ans)