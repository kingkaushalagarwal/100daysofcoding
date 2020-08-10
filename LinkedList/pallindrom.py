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
    def findMid(self):
        fast = self.head
        slow = self.head
        parent = None
        while fast!=None and fast.next!=None and slow!=None:
            fast =fast.next.next
            parent = slow
            slow=slow.next
        return [parent,slow,fast]
    #1,    2,    3 ,     4,    5 ,  6
    # f0s0  s1    s2f1       f2
    def reverse(self,root,node):
        if root==None:
            return None
        prev = None
        while prev!=node:
            temp=root.next
            root.next = prev
            prev = root
            root = temp
        return

    def printLL(self,root):
        print("values present in ll :",end=" ")
        while root!=None:
            print(root.val,end=" ")
            root = root.next
        print()
    def findPalin(self):
        self.printLL(self.head)
        root =  self.head
        parent,slow,fast = self.findMid()
        if parent==None:
            return 1
        if fast==None:
            r1 = parent
            r2 = slow
        else:
            r1=parent
            r2=slow.next
        print(r1.val,r2.val)
        self.reverse(self.head, r1)

        self.printLL(r1)
        self.printLL(r2)

        while r1!=None and r2!=None:
            if r1.val!=r2.val:
                return 0
            r1 = r1.next
            r2 =r2.next
        return 1

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(3)
ll.add(2)
ll.add(1)
ans  = ll.findPalin()
print("ans :",ans)
