class Solution:
	# @param A : list of integers
	# @return an integer
	#count 01 adjacent pair
   def bulbs(self, A):
        zero = 0
        one = 0;
        count = 0
        for x in A:
            if zero == 0 and x == 0:
                zero = 1
                count += 1
            if zero == 1 and x == 1:
                count += 1
                zero = 0
        return count

