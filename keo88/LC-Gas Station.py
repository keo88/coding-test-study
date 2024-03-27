class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cal = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(cal) < 0:
            return -1
        
        acc = idx = 0
        for i in range(len(cal)):
            acc += cal[i]
            if acc < 0:
                acc, idx = 0, i + 1
        return idx

