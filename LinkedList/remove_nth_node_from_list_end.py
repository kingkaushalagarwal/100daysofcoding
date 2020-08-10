"""
Better approach :- Make the first pointer go n nodes. Then move the second and first pointer simultaneously. This way,
the first pointer is always ahead of the second pointer by n nodes. So when first pointer reaches the end, you are on
the node to be removed
"""
class Solution:
    def removeNthFromEnd(self, root, n):
        if root == None:
            return
        first = root
        second = root
        count = 0
        while first != None and count < n:
            first = first.next
            count += 1
        if first == None:
            return root.next
        while first.next != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return root

