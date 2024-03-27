class Solution(object):

    def reverse(self, arr, i, j):
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i += 1
            j -= 1
    
    def rotate(self, nums, k):

        l = len(nums)
        k %= l

        dv = l - k

        self.reverse(nums, 0, dv - 1)
        self.reverse(nums, dv, l - 1)
        self.reverse(nums, 0, l - 1)
