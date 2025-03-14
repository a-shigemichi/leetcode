from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        Find the maximum product of lengths of two words that don't share any characters.
        
        Parameters:
        words (List[str]): List of words
        
        Returns:
        int: Maximum product of lengths, or 0 if no such pair exists
        """
        n = len(words)

        char_sets = [set(word) for word in words]
        
        max_prod = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if not char_sets[i].intersection(char_sets[j]):
                    prod = len(words[i]) * len(words[j])
                    max_prod = max(max_prod, prod)
        
        return max_prod
    