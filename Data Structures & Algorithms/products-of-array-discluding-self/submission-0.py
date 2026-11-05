class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left = 1
        right = 1
        
        # Calculate left product: nums[0] * nums[1]x ... nums[i-1]
        for i, n in enumerate(nums):
            res[i] = left
            left *= n

        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res






        