def generateValidParanthesis(l,left,right):
    #base condition
    if left==0:
        l=l+[')']*right
        right =0
        print(''.join(l))
    if left>0:
        generateValidParanthesis(l+['('],left-1,right)
    if left<right:
        generateValidParanthesis(l+[')'],left,right-1)


#Driver Code
n = int(input())
l= []
generateValidParanthesis(l,n,n)
