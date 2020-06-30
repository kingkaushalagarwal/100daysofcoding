#Interview Bit
#Area under the hills
class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        A.append(0)
        y1=0
        area=0
        for y2 in A:
            if y1==y2:
                area +=y1
            elif y1==0:
                area += 0.5*y2
            elif y2==0 and y1!=0:
                area += 0.5*y1
            elif y1<y2:
                area += (y2-y1)*0.5 + y1
            elif y1>y2:
                area += (y1-y2)*0.5 + y2
            y1= y2
            
        return str(int(area))        
            
            
