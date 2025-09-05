from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Calculate the sum of XOR totals for all subsets of the given array.
        
        Args:
            nums: List of integers
            
        Returns:
            Sum of XOR totals for all subsets
        """
        n = len(nums)
        total_sum = 0
        
        for i in range(1 << n):
            xor_total = 0
            for j in range(n):
                if i & (1 << j):
                    xor_total ^= nums[j]
            total_sum += xor_total
        
        return total_sum
