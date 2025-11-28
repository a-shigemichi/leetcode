class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Build an array where each element is determined by using the current element as an index.
        
        Args:
            nums: A zero-based permutation array of distinct integers from 0 to n-1
            
        Returns:
            An array ans where ans[i] = nums[nums[i]] for each index i
        """
        return [nums[nums[i]] for i in range(len(nums))]
