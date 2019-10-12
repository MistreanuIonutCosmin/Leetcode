"""
Problem:
Given a sorted array nums, remove the duplicates in-place such that each element 
appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the 
input array in-place with O(1) extra memory.

tests:
a) 1 2 3 4 
b) 1 1 1 1 
c) 1 1 2 2 
d) 1 2 2 2
e) 1 1
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_indx = 0
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[curr_indx] == nums[i]:
                i += 1
            if i < len(nums) and curr_indx < i - 1 :
                nums[curr_indx + 1] = nums[i]
            
            if i < len(nums):
                i += 1
                curr_indx += 1
            
        return curr_indx + 1
            
"""
Algorithm

Since the array is already sorted, we can keep two pointers i and j, where i is the slow-runner 
while j is the fast-runner. As long as nums[i] = nums[j], we increment j to skip the duplicate.

When we encounter nums[j] != nums[j], the duplicate run has ended so we must copy its value to 
nums[i + 1]. i is then incremented and we repeat the same process again until j reaches the end of array.
""" 

class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1
            