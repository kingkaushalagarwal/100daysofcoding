class  Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add(self,val):
        if self.head == None:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(val)

    def check(self,r1,r2):
        if r1==None or r2==None:
            return 0
        if r1.val==r2.val:
            return self.check(r1.next,r2.next)+2
        else:
            return 0

    def longestPalin(self):
        root = self.head
        length =1
        prev = None
        while root!=None:
            temp = root.next
            root.next = prev
            prev = root
            c1 = self.check(root,temp)
            c2 = self.check(root.next,temp) + 1
            length = max(length,c1,c2)
            root = temp
        return length


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(2)
ll.add(3)
ll.add(2)
ll.add(1)
ans  = ll.longestPalin()
print("ans :",ans)
