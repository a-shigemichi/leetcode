from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Given an array of integers nums, sort the array in increasing order 
        based on the frequency of the values. If multiple values have the 
        same frequency, sort them in decreasing order.
        
        Args:
            nums: List of integers to sort
            
        Returns:
            List sorted by frequency (ascending), then by value (descending)
        """
        # Count frequencies
        freq_count = Counter(nums)

        # Sort by frequency (ascending), then by value (descending)
        # We use tuple (frequency, -value) as key: frequency for primary sort,
        # negative value for secondary descending sort
        return sorted(nums, key=lambda x: (freq_count[x], -x))
