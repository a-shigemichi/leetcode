from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        Find all words that match the given pattern.
        
        A word matches the pattern if there exists a bijection from the pattern's letters
        to the word's letters.
        
        Args:
            words: List of strings to check against the pattern
            pattern: The pattern string
            
        Returns:
            List of words that match the pattern
        """
        def matches(word, pattern):
            if len(word) != len(pattern):
                return False

            p_to_w = {}
            w_to_p = {}
            
            for w_char, p_char in zip(word, pattern):
                if p_char in p_to_w:
                    if p_to_w[p_char] != w_char:
                        return False
                elif w_char in w_to_p:
                    if w_to_p[w_char] != p_char:
                        return False
                else:
                    p_to_w[p_char] = w_char
                    w_to_p[w_char] = p_char
                    
            return True
            
        return [word for word in words if matches(word, pattern)]
        