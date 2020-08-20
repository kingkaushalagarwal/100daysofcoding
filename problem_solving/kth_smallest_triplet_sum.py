class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def bruteForce(self,A,B):
        A.sort()
        count =B
        l = []
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                for k in range(j+1,len(A)):
                    l.append([A[i]+A[j]+A[k],i,j,k])
        l.sort()
        return l[B-1]

    def nc2(self, n):
        return (n * (n - 1)) // 2

    def solve(self, A, B):
        N = len(A)
        A.sort()
        i = 1
        val = self.nc2(N - i - 1)
        while B > val:
            B -= val
            i += 1
            val = self.nc2(N - i - 1)
        ans = A[i]
        print(i,A[i])
        j = i + 1
        l = []
        for j in range(i + 1, len(A)):
            for k in range(j + 1, len(A)):
                l.append(A[j] + A[k])
        l.sort()
        print(B)
        for i in range(len(l)):
            print(i,l[i])
        print(A[i],l[B-1])
        return A[i] + l[B - 1]


A = [ 22, 10, 5, 11, 16, 2, 11, 7, 16, 2, 17, 6, 15, 3, 9, 6 ]
B = 183
print(len(A))
S = Solution()
ans =S.solve(A,B)
print(ans)
ans  = S.bruteForce(A,B)
print(ans)