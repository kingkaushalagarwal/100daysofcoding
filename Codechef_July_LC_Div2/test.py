from copy import deepcopy
from testInput import input;
for _ in range(int(input())):
    n, x = map(int,input().split())
    count =0
    original = list(map(int,input().split()))
    arr = deepcopy(original)
    arr.sort()
    # print(arr)
    i=0
    original.sort()
    while i<len(arr):
      if arr[i]>x:
          arr[i]-=x
          arr[i]= min(original[i],arr[i]*2)
      elif arr[i]<=x:
          arr[i]=0
          i+=1
      x=2*x
      count+=1
      print(arr)
    print(count)
    # # print(arr)
    # while(len(arr)!=0):
    #     greater = None
    #     smaller = None
    #     maxx = None
    #     for i in range(len(arr)):
    #         y = arr[i]
    #         #finding element which is equal to or just greater than x
    #         if y>=x:
    #             if greater==None:
    #                 greater = i
    #             else:
    #                 if arr[greater]>y:
    #                     greater = i
    #         if y<x:
    #             if smaller==None:
    #                 smaller = i
    #             else:
    #                 if arr[smaller]<y:
    #                     smaller = i
    #         #finding maximum element of array
    #         if maxx==None:
    #             maxx= i
    #         else:
    #             if arr[maxx]<y:
    #                 maxx = i
    #     #population greater than and equal to x exists
    #
    #     if greater!=None:
    #         if smaller !=None and arr[smaller]!=0 and 2*arr[smaller]>x:
    #             # print("smaller")
    #             print(smaller, arr[smaller], x, arr)
    #             # x = 2 * arr[smaller]
    #             arr[smaller] = 0
    #         else:
    #             arr[greater]-=x
    #             arr[greater] = min(2*arr[greater],original[greater])
    #             print(greater,arr[greater],x,arr)
    #         x = 2 * x
    #         count += 1
    #
    #     else:
    #         print(len(arr),"no more greater", arr)
    #         # print(arr)
    #         for x in arr:
    #             if x>0:
    #                 count+=1
    #         break
    # print(count)
    #
    #
    #
    #
