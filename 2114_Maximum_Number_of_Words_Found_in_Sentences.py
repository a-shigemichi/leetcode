from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        """
        Find the maximum number of words that appear in a single sentence.
        
        A sentence is a list of words separated by a single space with no 
        leading or trailing spaces.
        
        Args:
            sentences: An array of strings where each string represents a single sentence
            
        Returns:
            The maximum number of words found in any single sentence
        """
        max_words = 0
        
        for sentence in sentences:
            word_count = len(sentence.split())
            max_words = max(max_words, word_count)
        
        return max_words
    