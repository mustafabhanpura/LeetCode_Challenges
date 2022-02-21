from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        collect = Counter(nums)
        
        for element in collect.keys():
            if collect[element] == 1:
                return element
            