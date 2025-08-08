from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        """
        Find the maximum number of pairs that can be formed from the array words.
        Two strings can be paired if one is the reverse of the other.
        
        Args:
            words: A 0-indexed array of distinct strings
            
        Returns:
            The maximum number of pairs that can be formed
        """
        seen = set()
        pairs = 0
        
        for word in words:
            reversed_word = word[::-1]
            
            if reversed_word in seen:
                pairs += 1
                seen.remove(reversed_word)
            else:
                seen.add(word)
        
        return pairs
