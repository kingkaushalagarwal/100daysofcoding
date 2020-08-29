from collections import deque
from math import ceil, log2;


def getMid(s,e):
    return s + (e-s)//2

def getSumUtil(tree, start, end, left, right, treeNode):
    if (left <=start and right >= end ):
        return tree[treeNode]
    if (end<left or start>right):
        return 0;
    if start!=end:
        mid = getMid(start,end)
        value=  getSumUtil(tree, start,mid, left, right, 2*treeNode+1)+ getSumUtil(tree, mid+1,end,left,right,2*treeNode+2)
        return value

def updateValueUtil(tree,start,end,i,diff,treeNode):
    if ( i<start or  i>end):
        return
    tree[treeNode] += diff;
    if(start!=end):
        mid = (start + end)//2
        updateValueUtil(tree,start,mid,i,diff,2*treeNode+1)
        updateValueUtil(tree,mid+1,end,i,diff,2*treeNode+2)


def updateValue(arr,tree,n,i,new_value):
    if (i<0 and i>n-1):
        print("Invalid input ",end=" ")
        return
    diff = new_value - arr[i];
    arr[i] = new_value
    updateValueUtil(tree,0,n-1,i,diff,0)



def getSum(tree, n,left,right):
    if (left<0 or right>n-1 or left >right):
        print("Invalid input ",end=" ")
        return -1;
    return getSumUtil(tree,0,n-1,left,right,0)


def constructSTUtil(arr,start,end,tree,treeNode):
    if start==end:
        tree[treeNode] =  arr[start]
        return arr[start]
    mid = getMid(start,end)
    tree[treeNode] = constructSTUtil(arr,start,mid,tree,2*treeNode+1) + constructSTUtil(arr,mid+1,end,tree,2*treeNode+2)
    return tree[treeNode]


def constructST(arr,n):
    x = (int)(ceil(log2(n)));
    max_size = 2*(int)(2**x)-1
    tree = [0]*max_size;
    constructSTUtil(arr,0,n-1,tree,0);
    return tree;

def printTree(tree):
    l = len(tree)
    queue = deque()
    queue.append(0)
    while len(queue)!=0:
        queue2 = deque()
        while len(queue)!=0:
            ind = queue.popleft()
            print(tree[ind],end="  ")
            if l>(2*ind+1):
                queue2.append(2*ind+1)
            if l>(2*ind+2):
                queue2.append(2 * ind + 2)
        print()
        queue = queue2
        queue2 = None

#Driver Code
if __name__=="__main__":
    arr = [1,3,5,7,9,11]
    n = len(arr)
    tree = constructST(arr,n)
    print("Sum of values in given range= ",getSum(tree,n,1,3))
    updateValue(arr,tree,n,1,10)
    print("Update sum of values in given range= ",getSum(tree,n,1,3),end= " ")
A= [3,1,4,5,25,6]
print([[x,i] for i,x in enumerate(A)])