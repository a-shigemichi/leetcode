class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix




def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    my_object = Solution()        
    judgement = my_object.setZeroes(matrix)
    print(judgement)

if __name__ == "__main__":
   main()