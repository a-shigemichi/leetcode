class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        """
        Find the number of unique k-diff pairs in the given array.
        A k-diff pair is a pair of integers (nums[i], nums[j]) where:
        - 0 <= i, j < len(nums)
        - i != j
        - |nums[i] - nums[j]| == k

        Args:
            nums (list[int]): An array of integers
            k (int): The target difference between pairs

        Returns:
            int: The number of unique k-diff pairs in the array
        """
        if k < 0:
          return 0
          
        seen = set()
        pairs = set()
        
        for num in nums:
            if num - k in seen:
                pairs.add(tuple(sorted([num, num-k])))
            if num + k in seen:
                pairs.add(tuple(sorted([num, num+k])))
            seen.add(num)
        
        return len(pairs)
