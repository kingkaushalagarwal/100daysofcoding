#InterviewBit remove duplicates from sorted array 2
class Solution:
    # @param A : list of integers
    # @return an integer
	def removeDuplicates(self,arr):
		if len(arr)<3:
			return len(arr)
		end = 1
		for i in range(2,len(arr)):
			if arr[i]!=arr[end -1]:
				end +=1 
				arr[end] = arr[i]
		return end + 1 		
    def removeDuplicates(self, arr):
        # arr =[1,2,3,4,5]
        i=0;j=0;num =None;count =0
        while i<len(arr) and j<len(arr):
            if num==None:
                num =arr[i]
                count = 1
                i+=1;j+=1
            else:
                if arr[j]==num:
        #            print(count)
                    count+=1
        
                    if i!=j:
                        arr[i],arr[j]=arr[j],arr[i]
                    if count<3:
                        i+=1;j+=1
                    else:
                        j+=1
        
                elif arr[j]!=num:
                    num = arr[j]
                    count =1
        
                    if i!=j:
                        arr[i],arr[j]=arr[j],arr[i]
        #            print(count)
                    i+=1;j+=1
        #        print(i,j,arr)
        return i