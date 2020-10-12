from testInput import input
class Solution:
    def find(self, u, parent):
        if parent[u] == u:
            return u
        par = self.find(parent[u], parent)
        parent[u] = par
        return par

    def union(self, u, v, height, parent):
        C = self.find(u, parent)

        D = self.find(v, parent)
        if (C == D):
            return False


        if height[C] > height[D]:
            parent[D] = C
        elif height[D] > height[C]:
            parent[C] = D
        else:
            height[C] += 1
            parent[D] = C
        return True


    def solve(self, A, B):
        parent = list(range(A + 1))
        height = [1] * (A + 1)
        B = sorted(B, key=lambda a: a[2],reverse = True)
        cost = 0
        for i in range(len(B)):
            u = B[i][0]
            v = B[i][1]
            if self.union(u, v, height, parent):
                cost += B[i][2]
        return cost
#
n,d = map(int,input().split())
arr =[]
for i in range(n):
    arr.append(list(map(int,input().split())))
B =[]
for i in range(n):
    for j in range(i+1,n):
        cost = 0
        for k in range(d):
            cost+=abs(arr[i][k]-arr[j][k])
        B.append([i+1,j+1,cost])
print(arr)
print(B)
ans = Solution().solve(n,B)
print(ans)
# print(2**38<998244353*240)