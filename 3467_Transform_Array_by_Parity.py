from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        """
        Transform array by replacing even->0, odd->1, then sort in non-decreasing order.
        
        Args:
            nums (List[int]): Input integer array
            
        Returns:
            List[int]: Transformed and sorted array
        """
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        nums.sort()
        
        return nums
    