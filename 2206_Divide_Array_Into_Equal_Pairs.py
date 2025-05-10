from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        Determine if the array can be divided into n pairs where each pair contains 
        equal elements.
        
        Args:
            nums (List[int]): An integer array consisting of 2 * n integers.
            
        Returns:
            bool: True if nums can be divided into n pairs where each pair contains
                  equal elements, False otherwise.
        """
        counter = Counter(nums)

        for count in counter.values():
            if count % 2 != 0:
                return False
                
        return True
    