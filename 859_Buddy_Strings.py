from typing import List

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
      """
      Determine if you can swap two letters in s so the result equals goal.
      
      Args:
          s (str): The source string
          goal (str): The target string
          
      Returns:
          bool: True if you can swap two letters in s to make it equal to goal, otherwise False
      """
      REQUIRED_SWAP_COUNT = 2
      if len(s) != len(goal):
          return False
      
      # If strings are already identical, need at least one duplicate character to swap. 
      # Check for duplicates using set.
      if s == goal:
          return len(set(s)) < len(s)

      differing_indices = self.differing_indices(s, goal)
      
      if len(differing_indices) != REQUIRED_SWAP_COUNT:
          return False
      
      first_diff_idx, second_diff_idx = differing_indices
      return s[first_diff_idx] == goal[second_diff_idx] and s[second_diff_idx] == goal[first_diff_idx]
    
    def differing_indices(self, s: str, goal: str) -> List[int]:
        """
        Find indices where characters in two strings differ.
        
        Args:
            s (str): First string to compare
            goal (str): Second string to compare
            
        Returns:
            list: A list of indices where characters differ
        """
        differing_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                differing_indices.append(i)

        return differing_indices
    

class TestSolution:
    def setup_method(self):
        self.solution = Solution()
    
    def test_buddyStrings_swap_makes_equal(self):
        # Test cases where swapping makes strings equal
        assert self.solution.buddyStrings("ab", "ba") == True
    
    def test_buddyStrings_with_identical_strings_having_duplicates(self):
        # Test cases where strings are already equal but have duplicates
        assert self.solution.buddyStrings("aa", "aa") == True
    
    def test_buddyStrings_with_identical_strings_no_duplicates(self):
        # Test cases where strings are already equal but have no duplicates
        assert self.solution.buddyStrings("abc", "abc") == False
    
    def test_buddyStrings_with_different_length_strings(self):
        # Test cases with different lengths
        assert self.solution.buddyStrings("abc", "abcd") == False
    
    def test_buddyStrings_with_more_than_two_differences(self):
        # Test cases with more than two differences
        assert self.solution.buddyStrings("abcd", "dcba") == False
    
    def test_buddyStrings_with_exactly_one_difference(self):
        # Test cases with exactly one difference
        assert self.solution.buddyStrings("abcd", "abfd") == False
    