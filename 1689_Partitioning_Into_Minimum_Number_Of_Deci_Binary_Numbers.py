class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Find the minimum number of positive deci-binary numbers needed to sum up to n.
        
        A deci-binary number is a decimal number whose digits are either 0 or 1 without any leading zeros.
        For example, 101 and 110 are deci-binary, while 112 and 3001 are not.
        
        Args:
            n: A string representing a positive decimal integer
            
        Returns:
            int: The minimum number of positive deci-binary numbers needed to sum up to n
        """
        return int(max(n))
    