from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        Calculate the minimum number of bricks crossed by drawing a vertical line.
        
        The function looks for the position where the maximum number of rows have an edge
        (gap between bricks), as this means fewer bricks will be crossed.
        
        Args:
            wall (List[List[int]]): A 2D array where each subarray represents a row of bricks,
                                  and each integer represents the width of a brick.
        
        Returns:
            int: The minimum number of bricks that must be crossed by a vertical line.
        
        Examples:
            >>> s = Solution()
            >>> s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2]])
            2
            >>> s.leastBricks([[1],[1],[1]])
            3
        """
        edge_counts = {}
        
        for row in wall:
            position = 0
            for brick in row[:-1]:
                position += brick
                edge_counts[position] = edge_counts.get(position, 0) + 1

        if not edge_counts:
            return len(wall)

        max_edges = max(edge_counts.values(), default=0)

        return len(wall) - max_edges