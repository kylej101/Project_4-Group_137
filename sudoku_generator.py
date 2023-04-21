class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells