# Solution 1: Sort and iterate O(nlong) complexity
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) > 1:
            for i in range(1, len(nums), 2):
                if nums[i] != nums[i - 1]:
                    return nums[i - 1]
                
            return nums[-1]
        else:
            return nums[0]
       
# Solution 2: HashTable - O(n) + O(n) = O(n) 
# Python dictionary is implemented as a hashTable
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int) # default value of int is 0
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i

# Solution 3: XOR O(n)
If we take XOR of zero and some bit, it will return that bit
a \oplus 0 = aa⊕0=a
If we take XOR of two same bits, it will return 0
a \oplus a = 0a⊕a=0
a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b

# XOR is associative and commutative
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
            
