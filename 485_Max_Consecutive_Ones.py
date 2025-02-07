class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:   
        """
        Find the maximum number of consecutive 1's in a binary array.
        
        Args:
            nums (list[int]): A binary array containing only 0's and 1's
            
        Returns:
            int: The length of the longest sequence of consecutive 1's
            
        """
        if not nums:
            return 0
        
        max_consecutive_count=0
        consecutive_count=0
        for num in nums:
            if num==1:
                consecutive_count+=1
                max_consecutive_count=max(consecutive_count,max_consecutive_count)
            else:
                consecutive_count=0
        
        return max_consecutive_count          
            