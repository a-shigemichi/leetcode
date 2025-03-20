from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        Find the length of the longest chain of pairs.
        
        A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c.
        
        Args:
            pairs: List of pairs where each pair is [left, right] and left < right
            
        Returns:
            The length of the longest chain that can be formed
            
        Example:
            Input: [[1,2], [2,3], [3,4]]
            Output: 2
            Explanation: The longest chain is [1,2] -> [3,4]
        """
        pairs.sort(key=lambda x: x[1])
        
        count = 0
        current_end = float('-inf')

        for start, end in pairs:
            if start > current_end:
                count += 1
                current_end = end
        
        return count