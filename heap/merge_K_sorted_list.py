#Interview Bit
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        root = None
        l = []
        for i in range(len(A)):
            l.append([A[i].val, i])
        heapq.heapify(l)
        while len(l) != 0:
            val, i = heapq.heappop(l)
            if root == None:
                temp = ListNode(val)
                root = temp
            else:
                temp.next = ListNode(val)
                temp = temp.next
            if A[i].next != None:
                A[i] = A[i].next
                heapq.heappush(l, [A[i].val, i])
        return root


