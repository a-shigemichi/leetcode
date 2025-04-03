from typing import List
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful

class Solution(object):
    def singleNumber(self, nums: List[int]) -> Result[int, str]:
        """
        Finds the element that appears exactly once in an array where all other elements appear exactly three times.
        
        Uses a bit manipulation approach that tracks bits appearing once and twice, automatically clearing bits that appear three times. 
        This implements a "mod 3 counter" for each bit position.
        
        Args:
            nums: A list of integers where all elements appear three times except for one element which appears once.
        
        Returns:
            A Result containing either:
            - Success: The integer that appears exactly once in the array.
            - Failure: An error message if the input array is empty.
        """
        # Check if the input array is empty
        if not nums:
            return Failure("Input array cannot be empty")
            
        bits_seen_once = 0
        bits_seen_twice = 0
        
        for current_num in nums:
            # Update the bits that have appeared once.
            bits_seen_once = (bits_seen_once ^ current_num) & ~bits_seen_twice
            # Update the bits that have appeared twice.
            bits_seen_twice = (bits_seen_twice ^ current_num) & ~bits_seen_once
        
        return Success(bits_seen_once)

class TestSolution:
    def setup_method(self):
        self.solution = Solution()
    
    def test_singleNumber_normal_case(self):
        # Test with an array where one element appears once and others appear three times.
        result = self.solution.singleNumber([2, 2, 3, 2])
        assert is_successful(result)
        assert result.unwrap() == 3

    def test_singleNumber_with_negative_numbers(self):
        # Test with negative numbers to verify that bitwise operations work correctly.
        result = self.solution.singleNumber([-2, -2, 3, -2])
        assert is_successful(result)
        assert result.unwrap() == 3
    
    def test_singleNumber_empty_array(self):
        # Test with an empty array.
        result = self.solution.singleNumber([])
        assert not is_successful(result)
        assert "Input array cannot be empty" in result.failure()
        