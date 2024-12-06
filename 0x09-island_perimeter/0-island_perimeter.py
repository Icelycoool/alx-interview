#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island described in a grid.

    Args:
        grid (list): A list of lists;
                     0 represents water while 1 represents land.

    Returns:
        int: perimeter of the island
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            # Check if current square is land
            if grid[i][j] == 1:
                perimeter += 4
                # Subtract 1 for each shared edge with a neighboring land cell
                # Top neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1

                # Left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1

                # Bottom neighbor
                if i < rows - 1 and grid[i+1][j] == 1:
                    perimeter -= 1

                # Rigth neighbor
                if j < cols - 1 and grid[i][j+1] == 1:
                    perimeter -= 1

    return perimeter
