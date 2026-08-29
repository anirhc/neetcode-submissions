class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        hashSet = set(nums)

        for n in nums:
            if (n - 1) not in hashSet:
                length = 1
                while (n + length) in hashSet:
                    length = length + 1
                res = max(length, res)

        return res        