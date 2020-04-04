class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, elem in enumerate(nums):
            if elem:
                nums[i] = 0
                nums[j] = elem
                j += 1
        
