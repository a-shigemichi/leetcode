class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        """
        Sort each matrix diagonal in ascending order.
        
        A matrix diagonal is a diagonal line of cells starting from some cell in either 
        the topmost row or leftmost column and going in the bottom-right direction until 
        reaching the matrix's end.
        
        Args:
            mat: An m x n matrix of integers.
            
        Returns:
            The matrix with each diagonal sorted in ascending order.
        """
        m, n = len(mat), len(mat[0])
        diagonals = {}
        
        for i in range(m):
            for j in range(n):
                if (i-j) not in diagonals:
                    diagonals[i-j] = []
                diagonals[i-j].append(mat[i][j])
        
        for k in diagonals:
            diagonals[k].sort()
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i-j].pop(0)
        
        return mat
    