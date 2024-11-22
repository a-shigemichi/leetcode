class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c, pos):
            if pos == len(word):
                return True
                
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or
                board[r][c] != word[pos] or
                board[r][c] == '#'):
                return False
                
            tmp = board[r][c]
            board[r][c] = '#'
            
            result = (dfs(r+1, c, pos+1) or
                    dfs(r-1, c, pos+1) or
                    dfs(r, c+1, pos+1) or
                    dfs(r, c-1, pos+1))
                    
            board[r][c] = tmp
            return result
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False        


def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    my_object = Solution()        
    judgement = my_object.exist(board,word)
    print(judgement)

if __name__ == "__main__":
   main()