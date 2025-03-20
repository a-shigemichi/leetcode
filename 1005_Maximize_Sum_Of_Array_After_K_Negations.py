from typing import List        
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        Find the largest possible sum after negating k elements.
        
        Args:
            nums: Array of integers
            k: Number of negation operations to perform
            
        Returns:
            The maximum possible sum after k negations
        """
        nums.sort()
        
        i = 0
        while k > 0 and i < len(nums) and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1

        if k > 0:
            if k % 2 == 1:
                nums.sort()
                nums[0] = -nums[0]

        return sum(nums)
    