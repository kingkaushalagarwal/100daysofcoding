#InterviewBit
#Inversion Count
class Solution:
    # @param A : list of integers
    # @return an integer
    
    def solve(self, arr):
        def mergeSort(arr,l,r):
            if l==r:
                return 0
            mid = (l+r)//2
            a = mergeSort(arr,l,mid)
            b = mergeSort(arr,mid+1,r)
            c = merge(arr,l,r,mid)
            return a+b+c
        def merge(arr,l,r,mid):
            B = [0]*(r-l+1)
            i=l;j=mid+1
            count =0;k=0
            while i<mid+1 and j<r+1:
                if arr[i]<=arr[j]:
                    count += j-(mid+1)
                    B[k]=arr[i]
                    i+=1
                else:
                    B[k]=arr[j]
                    j+=1
                k+=1
            while i<mid+1:
                count += j-(mid+1)
                B[k]=arr[i]
                i+=1;k+=1
            while j<r+1:
                B[k] = arr[j]
                j+=1;k+=1
            k=0
            for i in range(l,r+1):
                arr[i]=B[k]
                k+=1
            return count
        return mergeSort(arr,0,len(arr)-1)%(10**9+7)
        