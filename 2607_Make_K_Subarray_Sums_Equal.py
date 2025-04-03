from typing import List

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        """
        Calculate the minimum number of operations to make all subarrays of length k have equal sum.
        
        Since the array is circular, this means that indices with the same remainder when divided
        by gcd(n, k) must have the same value in the final array.
        
        Args:
            arr (List[int]): A 0-indexed circular integer array.
            k (int): The subarray length.
            
        Returns:
            int: The minimum number of operations to make all length-k subarrays have equal sum.
        """
        n = len(arr)
        g = self.gcd(n, k)
        
        total_ops = 0
        
        for i in range(g):
            group = []
            for j in range(i, n, g):
                group.append(arr[j])
            
            group.sort()
            
            median = group[len(group) // 2]
            
            for num in group:
                total_ops += abs(num - median)
        
        return total_ops
    
    def gcd(self, a: int, b: int) -> int:
        """Calculate the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a