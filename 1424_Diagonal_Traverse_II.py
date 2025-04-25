class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        """
        Return all elements of the 2D array in diagonal order.
        
        Elements are visited diagonally from top-left to bottom-right,
        with elements on the same diagonal visited from bottom-left to top-right.
        
        Args:
            nums: A 2D integer array where rows can have different lengths.
            
        Returns:
            A list of all elements in diagonal order.
        """
        diagonals = {}
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(nums[i][j])
        
        result = []
        for diagonal in sorted(diagonals.keys()):
            result.extend(diagonals[diagonal][::-1])
        
        return result
    