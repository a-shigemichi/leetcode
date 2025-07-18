from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        Find the maximum total sum that building heights can be increased by
        without changing the city's skyline from any cardinal direction.
        
        The skyline constraint means:
        - From north/south: each column's max height must remain the same
        - From east/west: each row's max height must remain the same
        
        For each building at (r,c), the maximum possible height is:
        min(max_height_in_row_r, max_height_in_column_c)
        
        Args:
            grid (List[List[int]]): n x n matrix representing building heights
            
        Returns:
            int: Maximum total increase in building heights
        """
        n = len(grid)

        row_max = [0] * n
        for i in range(n):
            row_max[i] = max(grid[i])

        col_max = [0] * n
        for j in range(n):
            col_max[j] = max(grid[i][j] for i in range(n))

        total_increase = 0
        for i in range(n):
            for j in range(n):
                max_possible_height = min(row_max[i], col_max[j])
                total_increase += max_possible_height - grid[i][j]
        
        return total_increase
