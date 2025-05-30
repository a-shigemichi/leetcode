from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """
        Find two duplicate numbers in the given list.
        
        Args:
            nums (List[int]): List containing integers from 0 to n-1 where exactly 
                            two numbers appear twice.
        
        Returns:
            List[int]: sneaky_nums - The two duplicate numbers in order of first duplicate occurrence.
        
        Example:
            >>> getSneakyNumbers([0, 1, 1, 0])
            [1, 0]
        """
        seen_nums = set()
        sneaky_nums = []
        
        for num in nums:
            if num in seen_nums:
                sneaky_nums.append(num)
            else:
                seen_nums.add(num)
                
        return sneaky_nums
    