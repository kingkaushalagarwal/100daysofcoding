import heapq
destination = 100
gas_present = 10
miles = [10, 20, 30, 60]
capacity = [60, 30, 30, 40]
def solve(destination,gas_present,miles,capacity):
    if gas_present<miles[0]:
        return -1
    count = 0
    pq =[]
    i=0
    heapq.heapify(pq)
    while (i<len(miles)):
        if gas_present>=destination:
            return count
        if miles[i]<=gas_present:
            heapq.heappush(pq,-capacity[i])
        else:
            value = heapq.heappop(pq)
            gas_present +=value
            count+=1
            if i+1<len(miles) and  gas_present<miles[i+1]:
                while len(pq)!=0 and gas_present<miles[i+1]:
                    value = heapq.heappop(pq)
                    gas_present += value
                    count+=1
                if gas_present<miles[i+1]:
                    return -1
            elif (i+1)==len(miles) and gas_present<destination:
                return -1

        i+=1
    return count
ans = solve(destination,gas_present,miles,capacity)
print(ans)