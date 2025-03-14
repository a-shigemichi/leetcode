from typing import List
import pytest

class PermutationElement:
    """
    A Class representing an element in a permutation, used as a structure.
    
    Attributes:
        num: The number in the permutation.
        position: The position of the number (1-indexed).
    """
    def __init__(self, num: int, position: int) -> None:
        self.num = num
        self.position = position

class Solution:
    def countArrangement(self, arrangement_size: int) -> int:
        """
        Count the number of beautiful arrangements possible with integers 1 to arrangement_size.
        
        A beautiful arrangement is a permutation of integers from 1 to arrangement_size where for each
        position i (1-indexed), either the number at position i is divisible by i,
        or i is divisible by the number at position i.
        
        Args:
            arrangement_size: The number of integers (1 to arrangement_size).
            
        Returns:
            The number of beautiful arrangements.
        """
        if arrangement_size <= 0:
            raise ValueError("arrangement_size must be a positive integer")
        
        # Define a constant for the starting position.
        FIRST_POSITION = 1

        # Track which numbers have been used.
        used_nums = [False] * (arrangement_size + 1)
        
        # Using a list for result since integers in Python are immutable.
        # This allows the count to be modified across recursive calls.
        beautiful_arrangement_count = [0]
        
        self.count_arrangements_backtrack(arrangement_size, FIRST_POSITION, used_nums, beautiful_arrangement_count)
        return beautiful_arrangement_count[0]

    def count_arrangements_backtrack(self, arrangement_size: int, position: int, used_nums: List[bool], beautiful_arrangement_count: List[int]) -> None:
        """
        Recursive backtracking function to build beautiful arrangements.
        
        Args:
            arrangement_size: The number of integers (1 to arrangement_size).
            position: Current position being filled (1-indexed).
            used_num: List tracking which numbers have been used.
            result: List with a single element to store the count.
        """
        if position > arrangement_size:
            beautiful_arrangement_count[0] += 1

        for num in range(1, arrangement_size + 1):
            if not used_nums[num]:
                perm_element = PermutationElement(num, position)
                
                if self.is_beautiful(perm_element):
                    # Mark the number as used.
                    used_nums[num] = True
                    # Continue filling the next position.
                    self.count_arrangements_backtrack(arrangement_size, position + 1, used_nums, beautiful_arrangement_count)
                    # Backtrack: mark the number as unused for other paths.
                    used_nums[num] = False
    
    def is_beautiful(self, perm_element: PermutationElement) -> bool:
        """
        Determine if the element satisfies the beautiful arrangement condition.
        
        Args:
            perm_element: A Permutation object with num and position attributes.
            
        Returns:
            bool: True if the element is part of a beautiful arrangement, False otherwise.
        """
        return (perm_element.num % perm_element.position == 0) or (perm_element.position % perm_element.num == 0)


class TestSolution:
    def setup_method(self):
        self.solution = Solution()
    
    def test_countArrangement_n1(self):
        # Test with arrangement_size = 1
        assert self.solution.countArrangement(1) == 1

    def test_countArrangement_n15(self):
        # Test with arrangement_size = 15
        assert self.solution.countArrangement(15) == 24679

    def test_countArrangement_negative(self):
        # Test with negative arrangement_size
        with pytest.raises(ValueError) as excinfo:
            self.solution.countArrangement(-5)
        assert "arrangement_size must be a positive integer" in str(excinfo.value)
