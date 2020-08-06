class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class holder:
    def __init__(self):
        self.left =None
        self.right = None 
def printf(root):
    temp =root
    while temp!=None:
        print(temp.data,end =" ")
        temp = temp.next
    print()
def reverse(root):
    holder.right = root
    holder.left = None
    while holder.right !=None:
        node1 = holder.right 
        node2 = holder.left 
        holder.left = holder.right
        holder.right = holder.right.next 
        node1.next = node2
    return holder.left    
    
root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
printf(root)
new_root = reverse(root)
printf(new_root)