#interview bit
#regular expression matching O(1) solution
def isMatch(A,B):
    n1 = len(A)
    n2 = len(B)
    if not n1 and not n2: return 1 
    if not n2:  return 0 
    i =0;j=0
    star = None 
    curr_i = None 
    while i<n1:
        if j<n2 and (A[i]==B[j] or B[j]=='?'):
            i+=1 
            j+=1 
        elif j<n2 and B[j] == '*':
            star = j 
            curr_i = i 
            j+=1 
        elif star is not None:
            i = curr_i 
            curr_i +=1 
            j = star + 1 
        else:
            return 0 
    while j<n2 and B[j]=='*':
        j+=1 
    return 1 if j==n2 else 0    
string = input()
pattern = input()
ans = isMatch(string,pattern)
print(ans)