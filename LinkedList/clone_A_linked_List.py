#Interview Bit
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.random = None

def clonelist(root1):
    if root1==None:
        return None
    temp1 = root1
    while temp1!=None:
        value = temp1.val
        new_node = ListNode(value)
        nextp = temp1.next
        temp1.next = new_node
        new_node.next = nextp
        temp1=temp1.next.next
    temp1 = root1
    root2 = None
    while temp1!=None:
        if temp1.random!=None:
            random = temp1.random
            temp1.next.random = random.next
        temp1 = temp1.next.next
    temp1=root1
    while temp1!=None:
        nextp = temp1.next
        temp1.next = temp1.next.next
        temp1 = temp1.next
        if root2==None:
            root2 = nextp
            temp2 = root2
        else:
            temp2.next = nextp
            temp2=temp2.next
    return root2
