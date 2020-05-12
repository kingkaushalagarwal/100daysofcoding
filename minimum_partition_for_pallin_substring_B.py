#InterviewBit
#find minimum number of partition required to make every substring as pallindrome
#BruteForce

def checkPallin(string,i,j):
    a=i;b=j
    while a<b:
        if string[a]!=string[b]:
            return False
        a+=1;b-=1
    return True        
def find(string, i,minn,length,store,ans):
    global dp
    if i==len(string):
        if minn[0]>length:
            minn[0]=length
            ans[0]=store
     
    for j in range(i,len(string)):
        if checkPallin(string,i,j):
            find(string,j+1,minn,length+1,store + [string[i:j+1]],ans)
            
        
string = "aba"
dp =[0]*len(string)
minn=[1000000];store =[];ans=[0]    
find(string,0,minn,0,store,ans)            
print(minn[0]-1)
print(ans[0])