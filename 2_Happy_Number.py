# Solution 1: recursion
from collections import defaultdict
class Solution:
    
    def __init__(self):
        self.dict = defaultdict(int)
    
    def isHappy(self, n: int) -> bool:

        # Termination criterion: sum is 1 or sum already in the dict 
        if n == 1:
            return True
        elif self.dict[n] != 0:
            return False
        
        self.dict[n] += 1
        
        # Break the number in a list of numbers
        chr_digits = list(str(n)) # ['1', '9']
        digits = map(int, chr_digits)
        squared_digits = [x ** 2 for x in digits]
        n = sum(squared_digits)
        
        return self.isHappy(n)

# Solution 2: Same as 1, but without recursion
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while (n:= sum(map(lambda x: int(x)**2, str(n)))) != 1 and not n in visited:
            visited.add(n)
        return not n in visited
      
# Solution 3: Space O(1) Solutions (Floyd's Cycle Detection Algorithm)
class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(num):
            return sum(map(lambda x:int(x)**2, str(num)))
        slow, fast = n, next_num(n)
        while (slow:=next_num(slow)) != (fast:=next_num(next_num(fast))) and fast != 1:
            continue
        return fast == 1 or not slow == fast
