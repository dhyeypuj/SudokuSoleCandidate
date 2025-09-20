def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()



sudoku_grid = []
print("Enter the Sudoku grid row by row (use 0 for empty cells):")
for i in range(9):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    sudoku_grid.append(row)

print("\nOriginal Sudoku:")
print_grid(sudoku_grid)

solved_grid = solve_sudoku_sole_candidate(sudoku_grid)
print("Sudoku after applying Sole Candidate strategy:")
print_grid(solved_grid)
