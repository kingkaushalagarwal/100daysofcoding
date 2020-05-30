#geeksforgeeks
#Longest Prefix Suffix
#https://practice.geeksforgeeks.org/problems/longest-prefix-suffix/0/
for t in range(int(input())):
    string = input()
    count = 0
    i=0
    j=1
    while j<len(string):    
        if string[i]==string[j]:
            count += 1
            i+=1
            j+=1
        elif string[i]!=string[j]:
            count = 0
            if i!=0:
                i = 0
            else:
                j+=1
    print(count)            
        