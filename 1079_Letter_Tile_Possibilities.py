from typing import List
from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Calculate the number of possible non-empty sequences of letters 
        that can be made using the given tiles.
        
        Args:
            tiles: A string where each character represents a tile with a letter
            
        Returns:
            The number of possible non-empty sequences
        """
        counter = Counter(tiles)
        
        def backtrack():
            total = 0
            
            for char in counter:
                if counter[char] > 0:
                    counter[char] -= 1
                    total += 1
                    total += backtrack()
                    counter[char] += 1
            
            return total
        
        return backtrack()