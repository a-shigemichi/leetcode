from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        Find all indices of words that contain the given character x.
        
        Args:
            words: A 0-indexed array of strings
            x: A character to search for in the words
            
        Returns:
            A list of indices representing words that contain character x.
            The returned array may be in any order.
        """
        result = []
        
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        
        return result
    