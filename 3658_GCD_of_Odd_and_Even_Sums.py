class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        """
        This function computes the GCD of two values:
        - The sum of the first n odd numbers
        - The sum of the first n even numbers
        
        Args:
            n: A positive integer representing how many odd and even numbers to sum.
            
        Returns:
            The greatest common divisor (GCD) of the two sums.
        """
        # Calculate sum of first n odd numbers: 1 + 3 + 5 + ... + (2n-1)
        # This can be simplified to n²
        sum_odd = n * n
        
        # Calculate sum of first n even numbers: 2 + 4 + 6 + ... + 2n
        # This can be simplified to n(n+1)
        sum_even = n * (n + 1)
        
        # Calculate GCD using Euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return gcd(sum_odd, sum_even)
