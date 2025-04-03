from typing import List

class Solution:
   def findNonMinOrMax(self, nums: List[int]) -> int:
       """
       Find a number that is neither the minimum nor the maximum in the array.
       
       Args:
           nums (List[int]): Array of distinct positive integers
           
       Returns:
           int: A number that is neither the minimum nor the maximum, or -1 if no such number exists.
       """
       if len(nums) <= 2:
           return -1
           
       min_val = min(nums)
       max_val = max(nums)
       
       for num in nums:
           if num != min_val and num != max_val:
               return num
               
       return -1