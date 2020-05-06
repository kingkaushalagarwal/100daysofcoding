#Basic linked list class

class Node: 
    def __init__(self,val ):
        self.val = val 
        self.next = None 
class LinkedList:
    def __init__(self):
        self.root = None 
    def insert(self,data):
        if self.root==None:
            self.root = Node(data)
        else:
            temp = self.root 
            while temp.next!=None:
                temp = temp.next 
            temp.next = Node(data)
    def printList(self):
        temp = self.root
        while temp!=None:
            print(temp.val,end=" ")
            temp = temp.next
        print()
ll = LinkedList()
ll.insert (1)
ll.insert (2)
ll.insert (3)
ll.insert (4)
ll.insert (5)
ll.insert (6)
ll.printList()
ll.printList()