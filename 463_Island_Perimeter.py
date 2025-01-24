class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        SINGLE_ISLAND_PERIMETER = 4

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += SINGLE_ISLAND_PERIMETER
                    if self.hasRightIsland(grid, row, col):
                        perimeter -= 2
                    if self.hasDownIsland(grid, row, col):
                        perimeter -= 2
          
        return perimeter
    
    def hasDownIsland(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row < len(grid)-1 and grid[row+1][col]
        
    def hasRightIsland(self, grid: List[List[int]], row: int, col: int) -> bool:
        return col < len(grid[0])-1 and grid[row][col+1]
