from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        """
        Find the first palindromic string in the array.
        
        A string is palindromic if it reads the same forward and backward.
        
        Args:
            words: List of strings to check
            
        Returns:
            str: First palindromic string found, or empty string if none exists
        """
        for word in words:
            if word == word[::-1]:
                return word
        return ""
