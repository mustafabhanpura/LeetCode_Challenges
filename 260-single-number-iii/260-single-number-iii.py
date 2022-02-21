from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        collect = Counter(nums)
        result = []
        
        for element in collect.keys():
            if collect[element] == 1:
                result.append(element)
            if len(result) == 2:
                return result
            
            
        
        
