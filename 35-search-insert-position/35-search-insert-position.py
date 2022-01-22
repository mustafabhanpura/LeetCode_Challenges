class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2

            if nums[mid]<target:
                start = mid+1
            else:
                if nums[mid] == target and nums[mid-1] != target:
                    return mid

                else:
                    end = mid - 1


        return start