from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        Count the number of passengers who are strictly more than 60 years old.
        
        Each string in details has the format:
        - First 10 characters: phone number
        - 11th character: gender
        - 12th-13th characters: age (2 digits)
        - 14th-15th characters: seat number
        
        Args:
            details: List of strings, each representing passenger information
            
        Returns:
            int: Number of passengers older than 60
        """
        count = 0
        
        for passenger in details:
            age_str = passenger[11:13]
            age = int(age_str)
            
            if age > 60:
                count += 1
        
        return count
    