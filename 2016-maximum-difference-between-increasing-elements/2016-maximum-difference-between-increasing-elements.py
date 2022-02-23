class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_number = 0
        max_number = 1
        
        max_diff = 0
        
        
        while max_number<len(nums):
            diff = nums[max_number]-nums[min_number]
            
            if nums[min_number]<nums[max_number]:
                max_diff = max(diff,max_diff)
            else:
                min_number = max_number
            max_number +=1
        
        if max_diff == 0:
            return -1
        
        return max_diff