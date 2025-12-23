from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Use hash sets to keep track of digits in each row, column and square
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        # Loop through each row and column, and we're going to check each cell
        # If the current value is a ".", we'll just skip it
        # Otherwise, we check that cell and see if its already in the rows set, the columns set, or the square set
        # If it is, it's a duplicate and we return false
        # If not, we add it to those sets

        # There are only 9 rows and columns

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue
                
                # Use floor division to get an exact integer
                if (board[row][column] in rows[row]
                or board[row][column] in columns[column] 
                or board[row][column] in squares[row // 3, column // 3]):
                    return False

                # Add the value to each row, column and square set so we can look it up later
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                squares[row // 3, column // 3].add(board[row][column])
            

        return True