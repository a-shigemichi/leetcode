from collections import Counter
from typing import List
import pytest

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        """
        Find the shortest completing word from a list of words based on a license plate.
        
        A completing word must contain all letters from the license plate (case-insensitive)
        with at least the same frequency, ignoring numbers and spaces in the license plate.
        
        Args:
            licensePlate (str): The license plate string containing letters, numbers, and spaces
            words (List[str]): List of candidate words
            
        Returns:
            str: The shortest word that contains all letters from the license plate.
                If multiple shortest words exist, returns the first one in the list.
        
        """
        shortest_word= ""
        shortest_word_length = float('inf')

        license_char_counts = self.count_alphabets(licensePlate)
        for word in words:
            if self.is_completing_word(word, license_char_counts) and len(word) < shortest_word_length:
                shortest_word = word
                shortest_word_length = len(word)

        return shortest_word


    def count_alphabets(self, licensePlate: str) -> Counter:
        """
        Extract characters from the license plate and count their occurrences
        
        Args:
            licensePlate (str): Input license plate string
            
        Returns:
            Counter: Counter object containing the count of each character 
                    (case-insensitive, ignoring numbers and spaces)
        
        Example:
            >>> get_license_char_count("1s3 PSt")
            Counter({'s': 2, 'p': 1, 't': 1})
        """
        license_chars = [c.lower() for c in licensePlate if c.isalpha()]

        return Counter(license_chars)
    
    
    def is_completing_word(self, word: str, license_count: Counter) -> bool:
        """
        Check if a word is a completing word for the license plate.
        A completing word must contain all characters from the license plate
        with at least the same frequency.
        
        Args:
            word (str): Word to check
            license_count (Counter): Counter object containing character counts
                                  from the license plate
        
        Returns:
            bool: True if the word is a completing word, False otherwise
        
        Example:
            >>> license_count = Counter({'s': 2, 'p': 1, 't': 1})
            >>> is_completing_word("steps", license_count)
            True
        """
        word_char_counts = Counter(word.lower())

        return all(
            word_char_counts[char] >= required_count 
            for char, required_count in license_count.items()
        )
    

class TestSolution:
   """Test cases for Shortest Completing Word problem"""
   
   def setup_method(self):
       """Set up a new Solution instance for each test"""
       self.solution = Solution()

   @pytest.mark.parametrize(
       "license_plate, words, expected",
       [
           (
               "1s3 PSt",
               ["step", "steps", "stripe", "stepple"],
               "steps"
           ),
           (
               "1s3 456",
               ["looks", "pest", "stew", "show"],
               "pest"
           ),
       ]
   )

   
   def test_shortest_completing_word(
       self,
       license_plate: str,
       words: List[str],
       expected: str
   ):
       """
       Test shortestCompletingWord function with various test cases.
       
       Args:
           license_plate: Input license plate string
           words: List of candidate words
           expected: Expected shortest completing word
       """
       assert self.solution.shortestCompletingWord(license_plate, words) == expected
