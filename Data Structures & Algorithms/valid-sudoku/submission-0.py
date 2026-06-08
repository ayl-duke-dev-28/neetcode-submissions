class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        squares = []

        for i in range(9):
            rows.append([])
            cols.append([])
            squares.append([])

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                square_index = (i//3) * 3 + (j//3)

                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[square_index]:
                    return False
                
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                squares[square_index].append(board[i][j])
            
        return True