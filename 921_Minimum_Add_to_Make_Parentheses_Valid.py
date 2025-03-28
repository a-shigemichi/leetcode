class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Calculate the minimum number of parentheses to add to make the string valid.
        
        A valid parentheses string must:
        - Be empty, or
        - Be of the form AB where A and B are valid strings, or
        - Be of the form (A) where A is a valid string
        
        Parameters:
            s (str): A string containing only '(' and ')'
            
        Returns:
            int: The minimum number of parentheses needed to make the string valid
        """
        parentheses_to_add = 0
        open_parentheses_count = 0
        
        for char in s:
            if char == '(':
                open_parentheses_count += 1
            else:
                open_parentheses_count -= 1
                
                if open_parentheses_count < 0:
                    parentheses_to_add += 1
                    open_parentheses_count = 0
        
        parentheses_to_add += open_parentheses_count
        
        return parentheses_to_add
    