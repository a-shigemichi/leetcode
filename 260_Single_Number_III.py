from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Finds all numbers that appear exactly once in the input list.
        
        This function examines all elements in the input list and identifies
        elements that appear exactly once. Other elements may appear two or more times.
        
        Args:
            nums (List[int]): A list of integers
            
        Returns:
            List[int]: A list of integers that appear exactly once in the input list
        """
        seen_once = set()
        seen_twice = set()
        
        for num in nums:
            if num in seen_once:
                seen_once.remove(num)
                seen_twice.add(num)
            elif num not in seen_twice:
                seen_once.add(num) 
                
        return list(seen_once)