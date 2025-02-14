class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if you can reach the last index of the array starting from index 0.
        Each element represents the maximum number of steps you can jump from that position.
        
        Args:
            nums (List[int]): Array where each element represents maximum jump length
            
        Returns:
            bool: True if last index can be reached, False otherwise
            
        """
        target = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        
        return target == 0