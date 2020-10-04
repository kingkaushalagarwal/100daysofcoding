#combination sum
#this solution beats 98% python solution
class Solution(object):
    def combination(self,candidates,target):
        result =[]
        candidates = sorted(candidates)
        def dfs(remain,stack):
            if remain==0:
                result.append(stack)
                return
            for item in candidates:
                if item>remain: break                 #if current item is greater than remaining items then all items occuring after it also greater then remaining item
                if stack and stack[-1]>item:continue  #for maintianing the increasing order of addition we do purning
                else:
                    dfs(remain-item,stack+[item])
        dfs(target,[])
        return result