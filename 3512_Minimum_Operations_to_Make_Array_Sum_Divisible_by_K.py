from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Return the minimum number of operations required to make the sum of the array
        divisible by k. Each operation decreases nums[i] by 1 (cannot go below 0).
        
        Args:
            nums (List[int]): Array of integers
            k (int): Target divisor
            
        Returns:
            int: Minimum number of operations needed
        """
        total_sum = sum(nums)
        remainder = total_sum % k
        
        if remainder == 0:
            return 0
        
        return remainder
