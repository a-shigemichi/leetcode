class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """
        Find all valid combinations of k numbers that sum to n using numbers 1-9.
        Each number is used at most once.
        
        Args:
            k: Number of elements in each combination
            n: Target sum
            
        Returns:
            List of all possible valid combinations
        """
        result = []
        
        def backtrack(start, current_sum, current_combination):
            if len(current_combination) == k and current_sum == n:
                result.append(current_combination[:])
                return
            
            if len(current_combination) >= k or current_sum > n:
                return
                
            if len(current_combination) + (9 - start + 1) < k:
                return
            
            for i in range(start, 10):
                current_combination.append(i)
                
                backtrack(i + 1, current_sum + i, current_combination)
  
                current_combination.pop()

        backtrack(1, 0, [])
        
        return result