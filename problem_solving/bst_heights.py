class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.bst = None

    def add(self, v):
        if self.bst == None:
            self.bst = Node(v)
        else:
            temp = self.bst
            prev = temp
            while temp:
                if temp.val > v:
                    prev = temp
                    temp = temp.left
                elif temp.val<v:
                    prev = temp
                    temp = temp.right
                else:
                    return
            if prev.val > v:
                prev.left = Node(v)
            else:
                prev.right = Node(v)

    def heightUtil(self, root,ans):
        if root == None: return 0
        if root.left == None and root.right == None:
            return 0
        value =  max(self.heightUtil(root.left,ans), self.heightUtil(root.right,ans)) + 1
        ans[0]+=value
        return value
    def height(self,ans):
        if self.bst == None:
            return 0
        root = self.bst
        value=  self.heightUtil(root,ans)
        return value
# n = int(input())
# arr = list(map(int, input().split()))return
n = 7
arr =[6,2,8,1,4,4,7]
# 7
# 6 2 8 1 4 4 7
T = BST()
for x in arr:
    T.add(x)
ans =[0]
print([T.height(ans),ans[0] ])
print(ans[0])