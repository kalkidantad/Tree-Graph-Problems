from typing import List
import collections

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = collections.deque()

        # Add all land cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # Edge case: If there is no water or the grid is all water
        if len(queue) == 0 or len(queue) == n * n:
            return -1

        # BFS to find the maximum distance
        distance = -1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # Check all 4 neighbors
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1  # Mark as visited
                        queue.append((x, y))
            distance += 1

        return distance


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Mixed land and water
    grid1 = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    print("Max distance (grid1):", solution.maxDistance(grid1))  # Output: 2

    # Example 2: Water surrounded by land
    grid2 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print("Max distance (grid2):", solution.maxDistance(grid2))  # Output: 1

    # Example 3: All water
    grid3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print("Max distance (grid3):", solution.maxDistance(grid3))  # Output: -1

    # Example 4: All land
    grid4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print("Max distance (grid4):", solution.maxDistance(grid4))  # Output: -1

    # Example 5: Larger grid with mixed values
    grid5 = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    print("Max distance (grid5):", solution.maxDistance(grid5))  # Output: 4
