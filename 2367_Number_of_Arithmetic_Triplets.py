from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        """
        Counts the number of unique arithmetic triplets in a strictly increasing array.
        
        An arithmetic triplet (i, j, k) satisfies:
        - i < j < k
        - nums[j] - nums[i] == diff
        - nums[k] - nums[j] == diff
        
        Args:
            nums (List[int]): A 0-indexed, strictly increasing integer array
            diff (int): A positive integer representing the common difference
            
        Returns:
            int: The number of unique arithmetic triplets
        """
        num_set = set(nums)
        count = 0
        
        for num in nums:
            if num + diff in num_set and num + 2 * diff in num_set:
                count += 1
                
        return count
