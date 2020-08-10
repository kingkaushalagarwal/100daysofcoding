#InterviewBit
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list

    def partition(self, root, B):
        if root == None:
            return

        head1 = None;
        tail1 = None
        head2 = None;
        tail2 = None
        temp = root
        while temp != None:
            if temp.val < B:
                if head1 == None:
                    head1 = temp
                    tail1 = temp
                else:
                    tail1.next = temp
                    tail1 = tail1.next

            else:
                if head2 == None:
                    head2 = temp
                    tail2 = temp
                else:
                    tail2.next = temp
                    tail2 = tail2.next
            temp = temp.next
            if tail1:
                tail1.next = None
            if tail2:
                tail2.next = None
        if head1 == None:
            return head2
        else:
            tail1.next = head2
            return head1


