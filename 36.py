class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        count_col = [{} for _ in range(9)]
        count_row = {}
        counts_box = [{} for _ in range(9)]
        ind_col=0
        ind_row=0
        box_ind = 0
        for row in range(9):
            count_row={}
            ind_col = 0
            if row % 3 == 0:
                ind_row += 1
            for col in range(9):
                if col % 3 == 0:
                    ind_col += 1
                if board[row][col] == ".":
                    continue
                else:
                    element = int(board[row][col])
                box_ind = 3*(ind_row-1)+ind_col-1
                if (element in count_row 
                    or element in count_col[col] 
                    or element in counts_box[box_ind]):
                    return False
                else:
                    count_row[element] = 1
                    count_col[col][element] = 1
                    counts_box[box_ind][element] = 1
        return True
        



def main():
    board = [
     ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    my_object = Solution()
    judgement = my_object.isValidSudoku(board)
    print(judgement)

if __name__ == "__main__":
    main()

