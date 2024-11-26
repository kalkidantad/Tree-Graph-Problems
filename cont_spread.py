from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        time = 0

        # Initialize the grid: add rotten oranges to the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Directions for neighboring cells
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform BFS
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Mark the orange as rotten
                        fresh -= 1       # Decrease the fresh orange count
                        rotten.append((nx, ny))  # Add the new rotten orange to the queue
            time += 1

        # If there are still fresh oranges left, return -1
        return -1 if fresh else time


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Basic grid with rot propagation
    grid1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    print("Time to rot all oranges (grid1):", solution.orangesRotting(grid1))  # Output: 4

    # Example 2: No fresh oranges
    grid2 = [
        [2, 2, 0],
        [0, 2, 2],
        [2, 0, 2]
    ]
    print("Time to rot all oranges (grid2):", solution.orangesRotting(grid2))  # Output: 0

    # Example 3: Impossible to rot all oranges
    grid3 = [
        [2, 1, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print("Time to rot all oranges (grid3):", solution.orangesRotting(grid3))  # Output: -1

    # Example 4: All fresh oranges
    grid4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print("Time to rot all oranges (grid4):", solution.orangesRotting(grid4))  # Output: -1

    # Example 5: Mixed grid with no fresh oranges
    grid5 = [
        [0, 2, 0],
        [0, 0, 0],
        [0, 2, 0]
    ]
    print("Time to rot all oranges (grid5):", solution.orangesRotting(grid5))  # Output: 0
