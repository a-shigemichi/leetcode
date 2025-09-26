from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Perform k operations on nums where each operation finds the minimum value
        and replaces it with the value multiplied by the multiplier.
        
        Args:
            nums: List of integers to perform operations on
            k: Number of operations to perform
            multiplier: The multiplier to apply to minimum values
            
        Returns:
            The final state of nums after all k operations
        """
        for _ in range(k):
            min_idx = nums.index(min(nums))
            nums[min_idx] *= multiplier
        return nums
