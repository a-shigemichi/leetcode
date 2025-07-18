
from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Generate a matrix where each element is the largest value in the 
        corresponding 3x3 submatrix of the input grid.
        
        Args:
            grid (List[List[int]]): n x n integer matrix where n >= 3
            
        Returns:
            List[List[int]]: (n-2) x (n-2) matrix with maximum values
        """
        n = len(grid)
        maxLocal = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = 0
                for di in range(3):
                    for dj in range(3):
                        max_val = max(max_val, grid[i + di][j + dj])
                row.append(max_val)
            maxLocal.append(row)
        
        return maxLocal
