from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
        Finds all k-distant indices in the given array.
        
        Args:
            nums: A 0-indexed array of integers.
            key: The target value to search for.
            k: The maximum distance between indices.
            
        Returns:
            A list of all k-distant indices sorted in increasing order.
        """
        key_indices = [i for i, num in enumerate(nums) if num == key]
        result = set()
        
        for j in key_indices:
            for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                result.add(i)
                
        return sorted(list(result))
