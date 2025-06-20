from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Count the number of good pairs where nums1[i] is divisible by nums2[j] * k.
        
        A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k,
        where 0 <= i <= n-1 and 0 <= j <= m-1.
        
        Args:
            nums1: First integer array of length n
            nums2: Second integer array of length m  
            k: A positive integer multiplier
            
        Returns:
            The total number of good pairs
        """
        count = 0
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
        
        return count
    