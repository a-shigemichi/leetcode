from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Find three numbers whose product is maximum and return the maximum product.
        
        Parameters:
        nums (List[int]): List of integers.
        
        Returns:
        int: Maximum product of three numbers from the list.
        """
        nums.sort()
        
        n = len(nums)
        
        # Two possible cases for maximum product:
        # 1. Product of three largest numbers (all positive or all negative)
        # 2. Product of two smallest numbers (both negative) and the largest number (positive)
        
        # Calculate both cases
        case1 = nums[n-1] * nums[n-2] * nums[n-3] 
        case2 = nums[0] * nums[1] * nums[n-1]
        
        # Return the maximum of the two cases
        return max(case1, case2)
    