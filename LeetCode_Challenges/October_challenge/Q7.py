#Rotate List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        temp = head
        length = 0
        while temp != None:
            temp = temp.next
            length += 1
        k = k % length
        if k == 0:
            return head
        num = length - k
        temp = head
        count = 1
        while count < num:
            temp = temp.next
            count += 1
        pointer = temp.next
        temp.next = None
        temp = pointer
        while temp.next != None:
            temp = temp.next
        temp.next = head
        head = pointer
        return head
