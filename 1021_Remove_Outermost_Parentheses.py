from typing import List

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        Removes the outermost parentheses from every primitive valid parentheses string
        in the primitive decomposition of the given string.
        
        A primitive valid parentheses string is a valid parentheses string that cannot
        be split into two nonempty valid parentheses strings.
        
        Args:
            s (str): A valid parentheses string consisting of '(' and ')' characters
            
        Returns:
            str: The string after removing outermost parentheses from each primitive component
        """
        result = []
        balance = 0
        start = 0
        
        for i, char in enumerate(s):
            if char == '(':
                balance += 1
            else:
                balance -= 1
                
            if balance == 0:
                primitive = s[start:i+1]
                if len(primitive) > 2:
                    result.append(primitive[1:-1])
                start = i + 1
        
        return ''.join(result)
