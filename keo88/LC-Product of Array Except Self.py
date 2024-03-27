class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = [0] * len(nums)
        asc = []
        dsc = []
        a, d = 1, 1

        for i in range(len(nums)):
            a *= nums[i]
            d *= nums[-i -1]
            asc.append(a)
            dsc.append(d)

        outputs[0] = dsc[-2]
        outputs[-1] = asc[-2]
        # print(asc, dsc, outputs)
        for j in range(1, len(nums) - 1):
            outputs[j] = asc[j - 1] * dsc[len(nums) - j - 2]
        return outputs

        
