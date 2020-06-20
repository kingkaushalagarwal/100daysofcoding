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
A = list(map(int,input().split()))
ans = solve(A)
print(ans)