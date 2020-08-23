class Solution:
    # @param A : root node of tree
    # @return an integer
    def check(self, string):
        count = 0
        for ch in string:
            if ch not in ['(', ')']:
                count += 1
        return True if count >= 2 else False

    def find(self, root, d, ans):
        if root and root.val == -1:
            return ""
        if ans[0] == True: return ""
        if root == None:
            return ""

        left = self.find(root.left, d, ans)

        # After getting right answer return
        if ans[0] == True: return ""

        right = self.find(root.right, d, ans)

        # After getting right answer return
        if ans[0] == True: return ""

        string = "(" + left + str(root.val) + right + ")"
        if left not in d:

            d[left] = 1
        elif self.check(left):
            ans[0] = True
            return ""
        if right not in d:
            d[right] = 1
        elif self.check(right):
            ans[0] = True
            return ""

        return string

    def solve(self, root):
        d = {}
        ans = [False]
        self.find(root, d, ans)
        # ans = self.dupSubUtil(root)
        return 1 if ans[0] else 0
