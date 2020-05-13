#interviewBit
'''
Let's Party
Problem Description
In Danceland, one person can party either alone or can pair up with another person. Can you find in how many ways they can party if there are A people in Danceland? Note: Return your answer modulo 10003, as the answer can be large.  


Problem Constraints
1 <= A <= 105


Input Format
Given only argument A of type Integer, number of people in Danceland.


Output Format
Return an integer denoting the number of ways people of Danceland can party.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        if n<3: return n
        m=10003
        p1=1;p2=2
        for i in range(3,n+1):
            ans=(p2%m+(p1%m*(i-1)%m)%m)%m
            p1=p2;p2=ans
        return ans%m
        