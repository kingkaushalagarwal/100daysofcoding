from collections import Counter
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def check(self, val, num, A):
        return True if sum(a // num for a in val) >= A else False

    def find(self, val, A):
        l = 1;
        h = 100000
        ans = [0]
        while l <= h:
            if l <= h:
                mid = (l + h) // 2
                if self.check(val, mid, A):
                    ans[0] = max(ans[0], mid)
                    l = mid + 1
                else:
                    h = mid - 1
        return ans[0]

    def solve(self, A, B):
        counter = Counter(B)
        val = sorted(list(counter.values()), reverse=True)
        val = val[:A]
        return self.find(val, A)
