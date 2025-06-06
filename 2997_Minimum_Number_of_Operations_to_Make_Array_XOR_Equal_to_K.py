from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Find the minimum number of bit flip operations to make XOR of all elements equal to k.
        
        Args:
            nums (List[int]): 0-indexed integer array
            k (int): target XOR value
            
        Returns:
            int: minimum number of bit flip operations needed
        """
        current_xor = 0
        for num in nums:
            current_xor ^= num

        diff = current_xor ^ k

        operations = 0
        while diff:
            operations += diff & 1
            diff >>= 1
        
        return operations