# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math

#  |  |  |
# [1, 2, 3, 4, 5, 6]

#            i: 5  
#            j: 3  
                
# middle_node : 4
#        head : 6

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        middle_node = head
        
        i = 0
        j = 0
        
        while(head.next):
            i += 1
            head = head.next

            if j  != math.ceil(i / 2):
                j = ceil(i / 2)
                middle_node = middle_node.next
                    
        return middle_node                  
