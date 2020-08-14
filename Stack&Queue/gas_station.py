def canCompleteCircuit(self, gas, cost):
    gas_present = 0
    gas_required = 0
    tank = 0
    start = 0
    for i in range(len(gas)):
        gas_present += gas[i]
        gas_required += cost[i]
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    if gas_present - gas_required < 0:
        return -1
    return start
