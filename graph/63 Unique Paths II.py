class Solution:
    """
    Time Limit Exceeded
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m and n and obstacleGrid[0][0] != 0:
            return 0

        return self.traveling(obstacleGrid, m, n, 0, 0)

    def traveling(self, grid, m, n, y, x):
        if m <= y or n <= x:
            return 0
        elif y == m - 1 and x == n - 1:
            return 1

        res = 0
        if y < m - 1 and grid[y + 1][x] == 0:
            res += self.traveling(grid, m, n, y + 1, x)
        if x < n - 1 and grid[y][x + 1] == 0:
            res += self.traveling(grid, m, n, y, x + 1)

        return res

    """
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m and n and obstacleGrid[0][0] != 0:
            return 0

        res = self.uniquePaths(m, n)
        cache = collections.defaultdict(list)
        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x] != 0:
                    to_path = self.uniquePaths(y + 1, x + 1)
                    from_path = self.uniquePaths(m - y, n - x)
                    res -= to_path * from_path
                    for prior in cache[(y,)]:
                        res += prior * from_path

                    for prior in cache[(None, x)]:
                        res += prior * from_path

                    cache[(y,)].append(to_path)
                    cache[(None, x)].append(to_path)

        return max(0, res)

    def uniquePaths(self, m: int, n: int) -> int:
        slot = m + n - 2
        return self.factory(slot, slot - n + 2) // self.factory(n - 1, 1)

    def factory(self, r, l):
        res = 1
        while l <= r:
            res *= l
            l += 1

        return res

    """
    Runtime: 55 ms, faster than 19.13% of Python3 online submissions for Unique Paths II.
    Memory Usage: 14.3 MB, less than 62.81% of Python3 online submissions for Unique Paths II.
    https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place).
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m and n and obstacleGrid[0][0] != 0:
            return 0

        obstacleGrid[0][0] = 1
        for y in range(1, m):
            obstacleGrid[y][0] = obstacleGrid[y - 1][0] * (1 - obstacleGrid[y][0])
        for x in range(1, n):
            obstacleGrid[0][x] = obstacleGrid[0][x - 1] * (1 - obstacleGrid[0][x])

        for y in range(1, m):
            for x in range(1, n):
                obstacleGrid[y][x] = (obstacleGrid[y - 1][x] + obstacleGrid[y][x - 1]) * (1 - obstacleGrid[y][x])

        return obstacleGrid[-1][-1]
