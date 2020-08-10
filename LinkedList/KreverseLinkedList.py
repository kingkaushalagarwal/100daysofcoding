#K reverse linked list from interview bit
class Solution:
    def reverse(self,root, n):
        right = root
        left = None
        while right != None and n > 0:
            node1 = right
            node2 = left
            left = right
            right = right.next
            node1.next = node2
            n -= 1
        return [left, right]

    def reverseIt(self,root, n):
        start = root
        end, new_start = self.reverse(root, n)
        final = end
        while new_start != None:
            end, temp = self.reverse(new_start, n)
            start.next = end
            start = new_start
            new_start = temp
        return final
    def reverseList(self, root, B):
        return self.reverseIt(root,B)
                
                
                
                
                