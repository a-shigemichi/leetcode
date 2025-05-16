class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Calculate the score of a string, defined as the sum of the absolute differences 
        between the ASCII values of adjacent characters.
        
        Args:
            s: A string to calculate the score for
            
        Returns:
            int: The score of the string
        """
        if not s or len(s) < 2:
            return 0
            
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
            
        return score
    