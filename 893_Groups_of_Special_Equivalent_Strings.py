from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        """
        Find the number of groups of special-equivalent strings.
        
        Two strings are special-equivalent if after any number of swaps of characters at even indices
        with other characters at even indices, or characters at odd indices with other characters at odd indices,
        they can become equal.
        
        Args:
            words: A list of strings of the same length
            
        Returns:
            The number of groups of special-equivalent strings
        """
        unique_signatures = set()
        
        for word in words:
            even_chars = ''.join(sorted(word[0::2]))
            odd_chars = ''.join(sorted(word[1::2]))

            signature = even_chars + '#' + odd_chars

            unique_signatures.add(signature)

        return len(unique_signatures)
    