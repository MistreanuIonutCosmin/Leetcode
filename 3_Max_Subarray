import math

class Solution:
        
    def maxSubArray(self, nums: List[int]) -> int:
        w_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1,len(nums)):
            w_sum = max(w_sum+nums[i], nums[i])
            max_sum = max(w_sum, max_sum)
        return max_sum
