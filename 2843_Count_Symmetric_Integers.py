class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Count symmetric integers in the given range.
        
        A symmetric integer has an even number of digits where the sum of 
        the first half equals the sum of the second half.
        
        Args:
            low: The lower bound of the range (inclusive)
            high: The upper bound of the range (inclusive)
            
        Returns:
            The count of symmetric integers in [low, high]
        """
        count = 0
        
        for num in range(low, high + 1):
            s = str(num)
            n = len(s)
            
            if n % 2 == 1:
                continue
            
            mid = n // 2
            first_half_sum = sum(int(digit) for digit in s[:mid])
            second_half_sum = sum(int(digit) for digit in s[mid:])
            
            if first_half_sum == second_half_sum:
                count += 1
        
        return count
