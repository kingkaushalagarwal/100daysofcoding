#interviewBit flip array
#knapsack approach to solve it.
class Node:
    def __init__(self,items,weight):
        self.items = items 
        self.weight = weight 
def solve(A):
    summ = sum(A)//2
    dp = [ [ Node(0,0)]*(summ+1)  for j in range(len(A)+1)]
    for i in range(len(A)+1):
        for j in range(1,summ+1):
            prev_item = dp[i-1][j].items 
            prev_weight = dp[i-1][j].weight 
            if j - A[i-1]>=0:
                curr_item = dp[i-1][j-A[i-1]].items + 1
                curr_weight = dp[i-1][j-A[i-1]].weight + A[i-1]
                if (curr_weight>prev_weight) or ((curr_weight==prev_weight) and (curr_item<prev_item)):
                    dp[i][j] = Node(curr_item,curr_weight)
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1].items 
#Driver Code 
# A = list(map(int,input().split()))
A =  [ 8, 4, 11, 7, 3, 9, 8, 6, 4, 6, 6, 11, 12, 8, 8, 4, 2, 6, 9, 7, 3, 3, 6, 2, 5, 5, 11, 4, 4, 9, 5, 3, 5, 7, 10, 7, 7, 5, 4, 10, 2, 9, 1, 1, 4, 12, 8, 10, 5, 4, 4, 12, 11, 9, 5, 7, 6, 4, 10, 9, 4, 6, 3, 8, 4, 12, 7, 2, 5, 10, 3, 10, 11, 3, 11, 6, 3, 10, 3, 11, 2, 7, 10 ]

ans = solve(A)
print(ans)