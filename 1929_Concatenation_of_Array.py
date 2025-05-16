class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Create a new array that is the concatenation of the input array with itself.
        
        Given an integer array nums, create an array ans where ans[i] = nums[i] and 
        ans[i + n] = nums[i] for 0 <= i < n, where n is the length of nums.
        
        Args:
            nums: An integer array of length n
            
        Returns:
            List[int]: A new array of length 2n that is the concatenation of nums with itself
        """
        return nums + nums
    