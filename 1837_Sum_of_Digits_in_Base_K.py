class Solution:
    def sumBase(self, n: int, k: int) -> int:
        """
        Convert integer n from base 10 to base k, then return the sum of its digits.
        
        Args:
            n: Integer in base 10
            k: Target base for conversion
            
        Returns:
            Sum of digits after conversion to base k
        """
        digit_sum = 0
        while n > 0:
            digit_sum += n % k
            n //= k
        return digit_sum
