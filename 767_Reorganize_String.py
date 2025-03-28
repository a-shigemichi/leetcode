from typing import List, Tuple
from collections import Counter
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful

class Solution:
    def reorganizeString(self, input_string: str) -> Result[str, str]:
        """
        Rearranges the characters of input_string so that no adjacent characters are the same.
        
        Args:
            input_string: The input string to rearrange.
        
        Returns:
            A Result containing either:
            - Success: The rearranged string where no adjacent characters are the same.
            - Failure: An error message indicating why the rearrangement failed (either "Input string cannot be empty" 
          or "Rearrangement is not possible").

        """
        # The problem constraints specify that the input string length must be at least 1.
        if not input_string:
            return Failure("Input string cannot be empty")
            
        counts = Counter(input_string)
        
        most_common_count = counts.most_common(1)[0][1]
        
        # If the most frequent character exceeds half of the string, rearrangement is not possible.
        if most_common_count > (len(input_string) + 1) // 2:
            return Failure("Rearrangement is not possible")
        
        return Success(self.arrange_characters(counts.most_common()))
    
    def arrange_characters(self, char_counts: List[Tuple[str, int]]) -> str:
        """
        Arranges characters alternately starting with even indices and then odd indices.
        
        Args:
            char_counts: A list of (character, count) pairs, sorted by frequency in descending order.
        
        Returns:
            A string where characters are arranged to avoid adjacent duplicates.
        """
        INDEX_STEP = 2
        ODD_IDX_START = 1

        chars_length = sum(count for _, count in char_counts)
        
        rearranged_chars = [''] * chars_length
        
        chars_index = 0
        
        for char, count in char_counts:
            for _ in range(count):
                rearranged_chars[chars_index] = char
                chars_index += INDEX_STEP
                if chars_index >= chars_length:
                    chars_index = ODD_IDX_START
                    
        return ''.join(rearranged_chars)


class TestSolution:
    def setup_method(self):
        self.solution = Solution()
    
    def test_reorganizeString_possible(self):
        # Test with a string that can be reorganized
        result = self.solution.reorganizeString("aab")
        # Check that the result is success
        assert is_successful(result)
        # Get the rearranged string
        rearranged = result.unwrap()
        # Check that no adjacent characters are the same
        for i in range(1, len(rearranged)):
            assert rearranged[i] != rearranged[i-1]
    
    def test_reorganizeString_impossible(self):
        # Test with a string that cannot be reorganized
        result = self.solution.reorganizeString("aaab")
        assert not is_successful(result)
        assert "Rearrangement is not possible" in result.failure()
    
    def test_reorganizeString_single_character(self):
        # Test with a single character
        result = self.solution.reorganizeString("a")
        assert is_successful(result)
        assert result.unwrap() == "a"
    
    def test_reorganizeString_empty(self):
        # Test with an empty string
        result = self.solution.reorganizeString("")
        # Should return an error for empty string
        assert not is_successful(result)
        assert "Input string cannot be empty" in result.failure()
