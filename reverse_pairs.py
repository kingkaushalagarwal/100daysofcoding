#InterviewBit
#Reverse Pairs
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def mergeSort(arr,l,r):
            if l==r:
                return 0
            mid = (l+r)//2
            a = mergeSort(arr,l,mid)
            b = mergeSort(arr,mid+1,r,)
            c = merge(arr,l,r,mid)
            return a+b+c
        def merge(arr,l,r,mid):
            B= []
            i=l;j= mid+1
            count =0;k=i
            while i<mid+1 and j<r+1:
                if arr[i]<=arr[j]:
                    B.append(arr[i])
                    i+=1
                else:
                    if arr[i]>2*arr[j]:
                        count += mid+1-i
                    else:
                        k = max(k,i)
                        while k<mid+1:
                            if arr[k]>2*arr[j]:
                                count += mid+1-k
                                break
                            k+=1
                    B.append(arr[j])
                    j+=1
            while i<mid+1:
                B.append(arr[i])
                i+=1
            while j<r+1:
                B.append(arr[j])
                j+=1
            k=0
            for i in range(l,r+1):
                arr[i]=B[k]
                k+=1
            return count            
        # arr =[1,10,3,8,2,0,5]
        # res = [0]*len(A)
        # rank = list(range(len(A)))
        return mergeSort(A,0,len(A)-1)
                