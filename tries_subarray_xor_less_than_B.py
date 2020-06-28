from math import log
class TreeNode(object):
    def __init__(self):
        self.zero = None
        self.one = None
        self.count = 1
class Tree(object):
    def __init__(self):
        self.root = None
    def insert(self,num,m):
        val = '{0:0'+ str(m) + 'b}'
        num = val.format(num)
        if self.root==None:
            self.root = TreeNode()
            temp = self.root
            for i in range(len(num)):
                v = int(num[i])
                if v==0:
                    temp.zero = TreeNode()
                    temp = temp.zero
                else:
                    temp.one = TreeNode()
                    temp = temp.one
        else:
            temp = self.root
            for i in range(len(num)):
                v = int(num[i])
                if v==0:
                    if temp.zero!=None:
                        temp = temp.zero
                        temp.count +=1
                    else:
                        temp.zero = TreeNode()
                        temp = temp.zero
                else:
                    if temp.one!=None:
                        temp = temp.one
                        temp.count +=1
                    else:
                        temp.one = TreeNode()
                        temp = temp.one

    def find(self,num,m,string):
        val = "{0:0" + str(m) + "b}"
        num = val.format(num)
        temp = self.root
        count = 0
        for i in range(len(num)):
            v1 = int(num[i]);
            v2 = int(string[i]);
            if v2==0:
                if v1==0:
                    if temp.zero!=None:
                        temp = temp.zero
                    else:
                        break
                elif v1==1:
                    if temp.one!=None:
                        temp = temp.one
                    else:
                        break
            elif v2==1:
                if v1==1:
                    if temp.one!=None:
                        count += temp.one.count
                    if temp.zero!=None:
                        temp = temp.zero
                    else:
                        break
                elif v1==0:
                    if temp.zero!=None:
                        count += temp.zero.count
                    if temp.one!=None:
                        temp = temp.one
                    else:
                        break
#            print("count",num,i,count)
        return count
    def printUtil(self,root,l):
        if root.zero==None and root.one==None:
            print(*l)
            return
        if root.zero!=None:
            self.printUtil(root.zero,l+[0])
        if root.one!=None:
            self.printUtil(root.one,l+[1])

    def printTree(self):
        l =[]
        temp = self.root
        self.printUtil(temp,l)
#arr=list(map(int,input().split()))
#B = int(input())
arr = [8, 3, 10, 2, 6, 7, 6, 9, 3]
B = 3
#arr = [9, 4, 3, 11]
#B = 7

prev =0
for i in range(len(arr)):
    arr[i] = arr[i]^prev
    prev = arr[i]
#print(arr)
#count=0
#for i in range(len(arr)):
#    for j in range(i+1,len(arr)):
#        if arr[i]^arr[j]<B:
#            count+=1
#print(count)
m = int(log(max(arr),2))+1
#print(m)
val = '{0:0' + str(m) + "b}"
string = val.format(B)
#print(string)
T = Tree()
T.insert(arr[0],m)
ans = 0
for i in range(1,len(arr)):
    temp= T.find(arr[i],m,string)
#    print("temp",temp,arr[i])
    ans+=temp
    T.insert(arr[i],m)
#print(ans)
for i in range(len(arr)):
    if arr[i]<B:
        ans+=1
print(ans)
#T.printTree()
#print(string)