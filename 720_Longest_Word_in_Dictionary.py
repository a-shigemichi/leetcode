from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
        Finds the longest word in the dictionary that can be built one character at a time
        from other words in the dictionary.
        
        Args:
            words (List[str]): Array of dictionary words
            
        Returns:
            str: Longest word that can be built incrementally or empty string if none exists
        """
        words.sort()
        
        word_set = set()
        result = ""
        
        for word in words:
            if len(word) == 1:
                word_set.add(word)
                if result == "":
                    result = word
            elif word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(result):
                    result = word
        
        return result
    