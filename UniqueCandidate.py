def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()

def find_possible_values(grid, row, col):
    if grid[row][col] != 0:
        return set()
    possible = set(range(1, 10))
    possible -= set(grid[row])
    possible -= {grid[r][col] for r in range(9)}
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    possible -= {grid[r][c] for r in range(start_row, start_row + 3)
                              for c in range(start_col, start_col + 3)}
    return possible
