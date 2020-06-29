#InterviewBit
#count of smaller numbers after self.
class Solution(object):
    def mergeSort(self,arr,l,r,index,res):
        if l==r:
            return
        mid = (l+r)//2
        self.mergeSort(arr,l,mid,index,res)
        self.mergeSort(arr,mid+1,r,index,res)
        self.merge(arr,l,r,mid,index,res)
    def merge(self,arr,l,r,mid,index,res):
        lsub =[]
        rsub =[]
        for i in range(l,mid+1):
            lsub.append(index[i])
        for i in range(mid+1,r+1):
            rsub.append(index[i])
        n1 = len(lsub)
        n2 = len(rsub)
        i,j = 0,0
        k= l
        while i<n1 and j<n2:
            if arr[lsub[i]]<=arr[rsub[j]]:
                res[lsub[i]]+=j
                index[k]=lsub[i]
                i+=1
                k+=1
            else:
                index[k] = rsub[j]
                j+=1
                k+=1
        while i<n1:
            res[lsub[i]]+=j
            index[k]= lsub[i]
            i+=1
            k+=1
        while j<n2:
            index[k] = rsub[j]
            j+=1
            k+=1


    def solve(self,arr):
        n = len(arr)
        index =list(range(n))
#        print(index)
        res =[0]*(n)
        self.mergeSort(arr,0,n-1,index,res)
        return res
