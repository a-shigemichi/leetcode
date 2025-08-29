from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Checks if two string arrays represent the same string when concatenated.
        
        Args:
            word1 (List[str]): First array of strings
            word2 (List[str]): Second array of strings
            
        Returns:
            bool: True if both arrays represent the same string when concatenated, False otherwise
        """
        return ''.join(word1) == ''.join(word2)
    