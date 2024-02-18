from bisect import bisect_left, bisect_right

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            localTarget = target - n
            insertInd = bisect_left(numbers, localTarget)

            if insertInd == len(numbers) or insertInd == i or numbers[insertInd] != localTarget:
                continue
            return sorted(map(lambda x: x + 1, [i, insertInd]))

        return []
