class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Find all unique combinations in candidates where the candidate numbers sum to target.
        Each number in candidates may only be used once in the combination.
        
        Args:
            candidates: List of candidate numbers
            target: Target sum
            
        Returns:
            List of all unique combinations that sum to target
        """
        candidates.sort()
        result = []
        
        def backtrack(start, current_sum, current_combination):
            if current_sum == target:
                result.append(current_combination[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                current_combination.append(candidates[i])

                backtrack(i + 1, current_sum + candidates[i], current_combination)

                current_combination.pop()

        backtrack(0, 0, [])
        
        return result