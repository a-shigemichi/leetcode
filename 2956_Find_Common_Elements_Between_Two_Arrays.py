class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the number of elements in nums1 that exist in nums2 and vice versa.
        
        Args:
            nums1: First integer array
            nums2: Second integer array
            
        Returns:
            A list containing [answer1, answer2] where answer1 is the count of 
            elements in nums1 that exist in nums2, and answer2 is the count of 
            elements in nums2 that exist in nums1.
        """
        set1 = set(nums1)
        set2 = set(nums2)
        
        answer1 = sum(1 for num in nums1 if num in set2)
        answer2 = sum(1 for num in nums2 if num in set1)
        
        return [answer1, answer2]
