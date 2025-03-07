from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Find all characters (including duplicates) that appear in all strings within words.
        
        Args:
            words: A list of strings
            
        Returns:
            A list of characters that appear in all strings (including duplicates)
        """
        if not words:
            return []

        char_counts = {}
        for char in words[0]:
            char_counts[char] = char_counts.get(char, 0) + 1

        for word in words[1:]:
            current_counts = {}
            for char in word:
                current_counts[char] = current_counts.get(char, 0) + 1

            for char in list(char_counts.keys()):
                if char in current_counts:
                    char_counts[char] = min(char_counts[char], current_counts[char])
                else:
                    del char_counts[char]
        
        result = []
        for char, count in char_counts.items():
            result.extend([char] * count)
        
        return result