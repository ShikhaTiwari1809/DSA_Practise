class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # Check rows
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != ".":
                    row.append(board[i][j])
            if len(row) != len(set(row)):
                return False
        
        # Check columns
        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != ".":
                    col.append(board[j][i])
            if len(col) != len(set(col)):
                return False

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != ".":
                            box.append(board[i][j])
                if len(box) != len(set(box)):
                    return False   

        
        return True
            
