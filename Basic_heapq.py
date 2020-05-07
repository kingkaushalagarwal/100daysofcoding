#heap queue in python4
'''
heap functions :
heapify(iterable) = convert the iterable into the heap
heappush(heap,ele)
heappop(heap)- remove and return the smallest element
heappushpop(heap,ele)-first push than pop
heappreplace(heap,ele)-first pop than push
nlargest(k,iterable,key=fun)
nsmallest(k,iterable,key=fun)
'''
import heapq
li =[5,7,9,1,3]
heapq.heapify(li)
print("the created list is :",end=" ")
print(list(li))
heapq.heappush(li,4)
print("the modified heap after push is :",end=" ")
print(list(li))
print("removing min using heappop ",heapq.heappop(li))
l1 = [5,7,9,4,3]
l2 = [5,7,9,4,3]
heapq.heapify(l1)
heapq.heapify(l2)
print("The popped item using heappushpop() is : ",end=" ")
print(heapq.heappushpop(l1,2))
print("The popped item using heapreplace() is :",end= " ")
print(heapq.heapreplace(l2,2))
li1 = [6,7,9,4,3,5,8,10,1]
print("the 3 largest numbers in list are: ",end=" ")
print(heapq.nlargest(3,li1))
print("the 3 smallest numbers in list are : ",end= " " )
print(heapq.nsmallest(3,li1))

