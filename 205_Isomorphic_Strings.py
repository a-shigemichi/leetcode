from typing import List
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful

class Solution:
    def is_isomorphic(self, word1: str, word2: str) -> Result[bool, str]:
        """
        Determines if two strings are isomorphic.
        
        Two strings are isomorphic if the characters in one string can 
        be replaced to get the other string. 
        All occurrences of a character must be replaced with another
        character while preserving the order of characters. 
        No two characters may map to the same character, 
        but a character may map to itself.
        
        Args:
            word1: First string to compare.
            word2: Second string to compare.
            
        Returns:
            Result[bool, str]: 
                Success(True) if the strings are isomorphic,
                Success(False) if the strings are not isomorphic,
                Failure with error message if strings are empty or have different lengths.
        """
        if not word1 or not word2:
            return Failure("Input strings cannot be empty")

        if len(word1) != len(word2):
            return Failure("Strings have different lengths")
        
        return Success(self.get_pattern(word1) == self.get_pattern(word2))

    def get_pattern(self, word: str) -> List[int]:
        """
        Converts a string into a pattern of indices representing 
        the first occurrence of each character.
        
        This creates a numerical pattern where each character is replaced
        by a unique ID based on when it first appears in the string.
        
        Args:
            word: String to convert into a pattern.
            
        Returns:
            List[int]: A list of integers representing the pattern of the string.
        """
        pattern = []
        char_to_id = {}
        unique_char_id = 0
        
        for character in word:
            if character not in char_to_id:
                char_to_id[character] = unique_char_id
                unique_char_id += 1
            pattern.append(char_to_id[character])
        
        return pattern
    

class TestSolution:
    def setup_method(self):
        self.solution = Solution()
    
    def test_is_isomorphic_success(self):
        # Test cases where strings are isomorphic and should return Success.
        result = self.solution.is_isomorphic("egg", "add")
        assert is_successful(result)
        assert result.unwrap() is True
    
    def test_is_isomorphic_failure(self):
        # Test cases where strings are not isomorphic and should return Failure.
        result = self.solution.is_isomorphic("foo", "bar")
        assert is_successful(result)
        assert result.unwrap() is False
    
    def test_is_isomorphic_empty(self):
        # Test with empty strings.
        result = self.solution.is_isomorphic("", "")
        assert not is_successful(result)
        assert "Input strings cannot be empty" in result.failure()
    
    def test_is_isomorphic_different_length(self):
        # Test with strings of different lengths.
        result = self.solution.is_isomorphic("abc", "ab")
        assert not is_successful(result)
        assert "Strings have different lengths" in result.failure()