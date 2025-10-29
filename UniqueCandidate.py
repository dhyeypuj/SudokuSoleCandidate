def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()

