from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        Creates a 2D array from nums where each row contains distinct integers
        and the number of rows is minimal.
        
        Args:
            nums (List[int]): An integer array
            
        Returns:
            List[List[int]]: A 2D array with minimal rows where each row has distinct integers
        """
        freq = Counter(nums)
        result = []
        
        while freq:
            row = []
            keys_to_remove = []
            
            for num in freq:
                row.append(num)
                freq[num] -= 1
                if freq[num] == 0:
                    keys_to_remove.append(num)
            
            for key in keys_to_remove:
                del freq[key]
            
            result.append(row)
        
        return result
    