#interview bit dp question
#find number of uniqe bst for given integer
'''
for any integer i
    calculate the sum of all tree when head is 1 to i
    for any head j:- head[j]= number_of_unique_left_subtree * number_of_unique_right_subtree
'''

# n = int(input())
arr =[0]*19
arr[0]=1
arr[1]=1
for i  in range(2,19):
    num = i//2
    summ=0
    for j in range(1,num+1):
        summ+=2*arr[j-1]*arr[i-j]
    if i&1:
        summ+= arr[num]**2
    arr[i]=summ
print(arr)