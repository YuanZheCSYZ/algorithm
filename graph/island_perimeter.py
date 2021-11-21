# 463 https://leetcode.com/problems/island-perimeter/

class Solution(object):
    """
    Runtime: 436 ms, faster than 76.55% of Python online submissions for Island Perimeter.
    Memory Usage: 13.6 MB, less than 73.63% of Python online submissions for Island Perimeter.
    """
    def islandPerimeter(self, grid):
        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    res += 4
                    if 0 <= y - 1:
                        res -= grid[y - 1][x]
                    if y + 1 < len(grid):
                        res -= grid[y + 1][x]
                    if 0 <= x - 1:
                        res -= grid[y][x - 1]
                    if x + 1 < len(grid[0]):
                        res -= grid[y][x + 1]

        return res

