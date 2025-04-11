from typing import List

class Solution:
    def reformat(self, s: str) -> str:
        """
        Reformat the string so that no letter is followed by another letter
        and no digit is followed by another digit.
        
        Args:
            s (str): The input alphanumeric string
            
        Returns:
            str: The reformatted string or empty string if impossible
        """
        letters = []
        digits = []
        
        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                digits.append(char)
        
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        result = []
        if len(letters) >= len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters
        
        for i in range(len(second)):
            result.append(first[i])
            result.append(second[i])
        
        if len(first) > len(second):
            result.append(first[-1])
        
        return ''.join(result)
    