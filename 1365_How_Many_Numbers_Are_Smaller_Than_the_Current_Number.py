from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        For each element in nums, count how many numbers in the array are smaller than it.
        
        Args:
            nums: List of integers
            
        Returns:
            List of integers where each element represents the count of smaller numbers
        """
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result
