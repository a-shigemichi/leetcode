from typing import List
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        Determine if it's possible to reorder the array such that arr[2*i+1] = 2*arr[2*i]
        for every 0 <= i < len(arr)/2.
        
        This means we need to pair elements where one is twice the other. Each element
        must belong to exactly one pair.
        
        Args:
            arr (List[int]): An integer array of even length.
            
        Returns:
            bool: True if it's possible to reorder the array to satisfy the condition,
                  False otherwise.
        """
        count = Counter(arr)

        for num in sorted(arr, key=abs):
            if count[num] == 0:
                continue

            if count[2 * num] < count[num]:
                return False

            count[2 * num] -= count[num]
            count[num] = 0
            
        return True
    