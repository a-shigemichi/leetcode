class Solution:
    def addDigits(self, num: int) -> int:
        """
        Add all digits of the number repeatedly until the result has only one digit.
        
        Args:
            num: A non-negative integer
            
        Returns:
            The digital root of the number
        """
        while num >= 10:
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10
                
            num = digit_sum
        
        return num
    