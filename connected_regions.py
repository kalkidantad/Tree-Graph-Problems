from typing import List

class Solution:
    def connectedRegions(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0  # Return 0 if the grid is empty

        rows, cols = len(grid), len(grid[0])  # Dimensions of the grid
        connected_regions = 0  # Counter for connected regions

        # Helper function to "sink" a region using DFS
        def sink(i, j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "1":
                print(f"Sinking cell ({i}, {j})")
                grid[i][j] = "0"  # Mark the cell as visited
                # Recursively visit adjacent cells
                sink(i + 1, j)  # Down
                sink(i - 1, j)  # Up
                sink(i, j + 1)  # Right
                sink(i, j - 1)  # Left
                return 1  # Increment region count for this call
            return 0  # No region to sink

        # Traverse every cell in the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":  # Start a new DFS if a "1" is found
                    print(f"Starting new region from cell ({i}, {j})")
                    connected_regions += sink(i, j)

        return connected_regions


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print("Number of connected regions:", solution.connectedRegions(grid1))
    # Output: 3

    # Example 2
    grid2 = [
        ["1", "0", "0"],
        ["0", "1", "0"],
        ["0", "0", "1"]
    ]
    print("Number of connected regions:", solution.connectedRegions(grid2))
    # Output: 3

    # Example 3
    grid3 = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    print("Number of connected regions:", solution.connectedRegions(grid3))
    # Output: 0

    # Example 4
    grid4 = [
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"]
    ]
    print("Number of connected regions:", solution.connectedRegions(grid4))
    # Output: 1
