    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid_unit(unit):
            unit = [i for i in unit if i != '.']
            return len(unit) == len(set(unit))
        
        def is_valid_row(board):
            for row in board:
                if not is_valid_unit(row):
                    return False
            return True
        
        def is_valid_column(board):
            for col in zip(*board):
                if not is_valid_unit(col):
                    return False
            return True
        
        def is_valid_box(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not is_valid_unit(box):
                        return False
            return True
        return is_valid_row(board) and is_valid_column(board) and is_valid_box(board)
