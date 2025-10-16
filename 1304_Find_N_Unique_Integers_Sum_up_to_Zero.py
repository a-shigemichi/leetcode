class Solution:
    def sumZero(self, n: int) -> List[int]:
        """
        This function generates an array of n unique integers that sum to zero.
        
        Args:
            n: A positive integer representing the size of the array to be generated.
            
        Returns:
            A list of n unique integers that sum to zero.
        """
        result = []
        
        # If n is odd, include 0 in the array
        if n % 2 == 1:
            result.append(0)
            
        # Add pairs of numbers that sum to zero
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
            
        return result
