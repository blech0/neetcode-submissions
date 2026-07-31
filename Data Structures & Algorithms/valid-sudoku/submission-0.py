class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for row in board:
            seen = set()
            for digit in row:
                if digit == ".":
                    continue
                if digit in seen:
                    return False
                seen.add(digit)

        # check columns
        for column in range(9):
            seen = set()
            for row in range(9):
                digit = board[row][column]
                if digit == ".":
                    continue
                if digit in seen:
                    return False
                seen.add(digit)
                
        # check sub boxes
        for box in range(9):
            seen = set()
            boxRow = (box // 3) * 3
            boxCol = (box % 3) * 3
            for dr in range(3):
                for dc in range(3):
                    digit = board[boxRow + dr][boxCol + dc]
                    if digit == ".":
                        continue
                    if digit in seen:
                        return False
                    seen.add(digit)

        return True