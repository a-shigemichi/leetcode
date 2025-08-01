import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        Finds the pivot integer x where sum(1 to x) = sum(x to n).
        
        Uses mathematical approach: if such x exists, then x = sqrt(n*(n+1)/2).
        This is derived from the equation: x*(x+1)/2 = (n*(n+1)/2) - (x*(x-1)/2)
        
        Args:
            n: int - The positive integer upper bound
            
        Returns:
            int - The pivot integer x, or -1 if no such integer exists
        """
        
        total_sum = n * (n + 1) // 2
        x = int(math.sqrt(total_sum))
        
        if x * x == total_sum:
            return x
        else:
            return -1
    
    def pivotIntegerBruteForce(self, n: int) -> int:
        """
        Alternative brute force solution for comparison.
        
        Checks each possible pivot by calculating left and right sums.
        Time complexity: O(n²), Space complexity: O(1)
        
        Args:
            n: int - The positive integer upper bound
            
        Returns:
            int - The pivot integer x, or -1 if no such integer exists
        """
        for x in range(1, n + 1):
            left_sum = x * (x + 1) // 2
            right_sum = n * (n + 1) // 2 - (x - 1) * x // 2
            
            if left_sum == right_sum:
                return x
        
        return -1