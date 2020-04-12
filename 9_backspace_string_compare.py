from collections import deque

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = deque()
        t = deque()
        
        for _s in S:
            if _s != "#":
                s.append(_s)
            elif len(s):
                s.pop()
    
        for _t in T:
            if _t != "#":
                t.append(_t)
            elif len(t):
                t.pop()
                
        print(list(s))
        print(list(t))
        
        return list(s) == list(t)
                
# def backspaceCompare(self, S: str, T: str) -> bool:
#         acc_s = 0
#         acc_t = 0
#         i = len(S) - 1
#         j = len(T) - 1
        
#         while (i >= 0 or j >= 0):            
#             if i >= 0:
#                 if S[i] == '#':
#                     acc_s += 1
#                     i -= 1
#                 elif acc_s:
#                     acc_s -= 1
#                     i -= 1
            
#             if j >= 0:
#                 if T[j] == '#':
#                     acc_t += 1
#                     j -= 1
#                 elif acc_t:
#                     acc_t -= 1
#                     j -= 1
            
#             if acc_s == 0 and acc_t == 0:
#                 if (i >= 0 and j >= 0 and S[i] != T[j]) or ((i == -1 or j == -1) and i != j):
#                     return False
#                 i -= 1
#                 j -= 1
            
#         return True

class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
