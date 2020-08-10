"""
Problem Description
Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.

Problem Constraints
1 <= |A| <= 106
1 <= B <= C <= |A|

Input Format
The first argument contains a pointer to the head of the given linked list, A.
The second arugment contains an integer, B.
The third argument contains an integer C.

Output Format
Return a pointer to the head of the modified linked list.

Example Input
Input 1:
 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 2
 C = 4
Input 2:
 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 1
 C = 5
Example Output
Output 1:
 1 -> 4 -> 3 -> 2 -> 5
Output 2:
 5 -> 4 -> 3 -> 2 -> 1
"""
from testInput import input
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
class LinkedList:
    def __init__(self):
        self.root = None
    def add(self,val):
        if self.root ==None:
            self.root=ListNode(val)
        else:
            temp = self.root
            while temp.next!=None:
                temp = temp.next
            temp.next = ListNode(val)
    def printList(self):
        if self.root==None:
            return
        temp = self.root
        while temp!=None:
            print(temp.val,end=" ")
            temp = temp.next
        print()
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, root, n1, n2):
        #if starting and integer is same return root
        if n1==n2:
            return root
        #checking whether n1 is at root node
        isFirst = False
        #if n1 is at root node then create pseudo root node
        if n1==1:
            newNode = ListNode(-10000)
            newNode.next = root
            root = newNode
            isFirst = True
            n1+=1
            n2+=1
        if n1>n2:
            n1,n2 = n2,n1

        temp1 = root;temp2 = root
        count=n1-1
        while temp1!=None and count>0:
            temp2 = temp1
            temp1 = temp1.next
            count-=1
        #checking whether n1 present or not in linked list
        if temp1==None:
            return root

        #actual reversal take place
        count =0
        while count<(n2-n1):
            temporary = temp1.next
            temp1.next = temp1.next.next
            temporary.next = temp2.next
            temp2.next = temporary
            count+=1
        if isFirst:
            return root.next
        return root

#Driver Code
A = list(input().split("->"))
B= int(input())
C = int(input())

ll = LinkedList()
for x in A:
    ll.add(int(x))
ll.printList()
ll.root = Solution().reverseBetween(ll.root,B,C)
ll.printList()
print("end ")
# print(ans)
