class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        Calculate the difference between the sum of integers not divisible by m
        and the sum of integers divisible by m in the range [1, n].
        
        Args:
            n: Upper bound of the range (inclusive)
            m: Divisor to check divisibility
            
        Returns:
            The difference num1 - num2 where num1 is the sum of non-divisible
            integers and num2 is the sum of divisible integers
        """
        num1 = 0
        num2 = 0
        
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        
        return num1 - num2
