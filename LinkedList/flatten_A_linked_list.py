"""
class ListNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.down=None
"""


# @param root: ListNode
# @return ListNode
def merge(a, b):
    if a == None and b == None:
        return None
    elif a == None:
        return b
    elif b == None:
        return a
    else:
        result = None
        if a.val < b.val:
            result = a
            result.down = merge(a.down, b)
        else:
            result = b
            result.down = merge(b.down, a)
        return result


def flatten(root):
    if root == None or root.right == None:
        return root
    return merge(root, flatten(root.right))
