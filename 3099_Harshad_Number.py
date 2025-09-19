class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        """
        Determines if x is a Harshad number and returns the sum of its digits if so.
        
        Args:
            x: The integer to check
            
        Returns:
            The sum of digits if x is a Harshad number, otherwise -1
        """
        digit_sum = sum(int(digit) for digit in str(x))
        return digit_sum if x % digit_sum == 0 else -1
