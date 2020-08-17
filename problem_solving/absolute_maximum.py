class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(A)
        arr = [A, B, C, D]

        # all positive or all negative
        ans = []
        maxx = float('-inf')
        minn = float('inf')
        maxx1 = float('-inf')
        minn1 = float('inf')

        for i in range(n):
            val = i
            val1 = i
            for j in range(4):
                val += arr[j][i]
                val1 -= arr[j][i]

            maxx = max(maxx, val)
            minn = min(minn, val)
            maxx1 = max(maxx1, val1)
            minn1 = min(minn1, val1)

        ans.append(abs(maxx - minn))
        ans.append(abs(maxx1 - minn1))

        # when one negative or three negative
        for k in range(4):
            maxx = float('-inf')
            minn = float('inf')
            maxx1 = float('-inf')
            minn1 = float('inf')

            for i in range(n):
                val = i
                val1 = i
                for j in range(4):
                    if j == k:
                        val -= arr[j][i]
                        val1 += arr[j][i]

                    else:
                        val += arr[j][i]
                        val1 -= arr[j][i]

                maxx = max(maxx, val)
                minn = min(minn, val)
                maxx1 = max(maxx1, val1)
                minn1 = min(minn1, val1)

            ans.append(abs(maxx - minn))
            ans.append(abs(maxx1 - minn1))

        # when two negative
        for k in range(4):
            for l in range(k + 1, 4):
                maxx = float('-inf')
                minn = float('inf')
                for i in range(n):
                    val = i
                    for j in range(4):
                        if j == k or j == l:
                            val -= arr[j][i]
                        else:
                            val += arr[j][i]
                    maxx = max(maxx, val)
                    minn = min(minn, val)
                ans.append(abs(maxx - minn))
        return max(ans)







