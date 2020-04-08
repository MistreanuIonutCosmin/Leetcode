
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = {}
        
        for i, string in enumerate(strs):
            sorted_string = "".join(sorted(string))
            if sorted_string not in _dict:
                _dict[sorted_string] = []
            
            _dict[sorted_string].append(string)
            
        result = []
        for key, value in _dict.items():
            result.append(value)
            
        return result
