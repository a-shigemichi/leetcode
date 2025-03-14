class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sort a string in decreasing order based on the frequency of characters.
        
        Parameters:
        s (str): The input string to be sorted
        
        Returns:
        str: A string sorted in decreasing order based on character frequency
        """
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        sorted_chars = sorted(s, key=lambda x: (-char_count[x], x))
 
        return ''.join(sorted_chars)
    