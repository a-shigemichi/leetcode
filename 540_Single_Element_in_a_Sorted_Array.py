class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left_idx, right_idx = 0, len(nums) - 1
        
        while left_idx < right_idx:
            mid_idx = left_idx + (right_idx - left_idx) // 2
            
            if mid_idx % 2 == 1:
                mid_idx -= 1
                
            if nums[mid_idx] != nums[mid_idx + 1]:
                right_idx = mid_idx
            else:
                left_idx = mid_idx + 2
                
        return nums[left_idx]