from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the next greater element for each element in nums1 within nums2.
        
        For each element in nums1, find the next greater element in nums2.
        The next greater element is the first element in nums2 which is greater
        than the current element and appears to its right.
        If no such element exists, return -1 for that element.
        
        Args:
            nums1 (List[int]): The first array of unique integers (subset of nums2)
            nums2 (List[int]): The second array of unique integers
            
        Returns:
            List[int]: Array where ans[i] is the next greater element for nums1[i] in nums2
        """
        next_greater = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num

            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        result = []
        for num in nums1:
            result.append(next_greater[num])
            
        return result