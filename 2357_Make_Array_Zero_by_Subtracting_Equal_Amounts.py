from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Calculate the minimum number of operations to make all elements in the array zero.
        
        In each operation:
        1. Choose a positive integer x that is less than or equal to the smallest non-zero element in the array
        2. Subtract x from every positive element in the array
        
        The optimal strategy is to always choose x equal to the smallest non-zero element.
        This results in the number of unique positive values in the array being the minimum number of operations.
        
        Parameters:
            nums (List[int]): An array of non-negative integers
            
        Returns:
            int: The minimum number of operations required to make all elements zero
        """
        unique_positives = set()
        for num in nums:
            if num > 0:
                unique_positives.add(num)
        
        return len(unique_positives)