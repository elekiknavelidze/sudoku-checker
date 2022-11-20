def is_valid_sudoku(board):
    """Determines whether a 9 x 9 Sudoku board is valid."""

    # This is a set that does not allow for duplicates and we use it for making
    # sure that we do not have repeating numbers in rows, columns, or 3 x 3 blocks
    seen_boxes = set()

    # We have 9 rows
    # 0 1 2 3 4 5 6 7 8 9
    for row in range(9):
        # We have 9 columns
        # 0 1 2 3 4 5 6 7 8 9
        for col in range(9):
            # We get the box by first getting the row and then getting the box itself
            # by indexing using the col variable from the loop
            box = board[row][col]

            # If the box is underscore ("_"), we skip it because we do not
            # use underscores for checking whether the Sudoku puzzle is valid
            if box == "_":
                continue

            # Marks are used for specifying where the box came from
            # A box comes from some row and some column
            #
            # Additionally, it also comes from some 3 x 3 block
            # To find which block it comes from we integer-divide the row
            # and the column by 3
            marks = {
                f"{box} found in row {row}",
                f"{box} found in col {col}",
                f"{box} found in block {row // 3, col // 3}",
            }

            # Check if we have already seen the row, column, or a block
            # Intersection will tell us if there is any common element between
            # marks and seen
            #
            # If we have already seen it, we return False because the Sudoku
            # puzzle is not valid
            if seen_boxes.intersection(marks) != set():
                return False

            # Add the row, the column, and the block to the seen set
            seen_boxes.update(marks)

    # If we never returned False, it means we had no issues and the Sudoku
    # puzzle is valid
    return True


# This is a wrong sudoku puzzle since we have two threes in the first row
board1 = [
    ["4", "3", "_", "_", "8", "_", "_", "3", "_"],
    ["6", "_", "_", "1", "9", "5", "_", "_", "_"],
    ["_", "9", "8", "_", "_", "_", "_", "6", "_"],
    ["8", "_", "_", "_", "6", "_", "_", "_", "3"],
    ["4", "_", "_", "8", "_", "3", "_", "_", "1"],
    ["7", "_", "_", "_", "2", "_", "_", "_", "6"],
    ["_", "6", "_", "_", "_", "_", "2", "8", "_"],
    ["_", "_", "_", "4", "1", "9", "_", "_", "5"],
    ["_", "2", "_", "_", "8", "_", "_", "7", "9"],
]

# This is a correct sudoku puzzle
board2 = [
    ["_", "_", "9", "_", "_", "2", "_", "5", "8"],
    ["1", "5", "2", "_", "_", "4", "_", "_", "3"],
    ["_", "_", "_", "_", "1", "5", "7", "_", "_"],
    ["5", "1", "_", "6", "_", "_", "8", "_", "_"],
    ["_", "8", "_", "_", "4", "1", "_", "3", "_"],
    ["_", "_", "6", "_", "_", "8", "_", "1", "4"],
    ["_", "_", "8", "_", "5", "7", "3", "_", "_"],
    ["_", "_", "_", "1", "_", "_", "4", "_", "7"],
    ["2", "3", "1", "4", "_", "_", "6", "_", "_"],
]

if is_valid_sudoku(board1) is True:
    print("Correct Sudoku Puzzle!")
else:
    print("Wrong Sudoku Puzzle!")

if is_valid_sudoku(board2) is True:
    print("Correct Sudoku Puzzle!")
else:
    print("Wrong Sudoku Puzzle!")
