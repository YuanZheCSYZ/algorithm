# https://leetcode.com/problems/spiral-matrix/

class Solution:
    """
    Runtime: 33 ms, faster than 23.39% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 14.2 MB, less than 59.34% of Python3 online submissions for Spiral Matrix.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        upper = 0
        lower = len(matrix)
        left = 0
        right = len(matrix[0])

        res = []
        while upper < lower and left < right:
            res.extend(matrix[upper][left:right])
            upper += 1

            if lower <= upper:
                break

            right -= 1
            for x in range(upper, lower):
                res.append(matrix[x][right])

            lower -= 1
            res.extend(reversed(matrix[lower][left:right]))

            if right <= left:
                break

            for x in range(lower - 1, upper - 1, -1):
                res.append(matrix[x][left])
            left += 1

        return res

    """
    Runtime: 29 ms, faster than 63.71% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 14 MB, less than 99.54% of Python3 online submissions for Spiral Matrix.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and list(matrix.pop(0)) + self.spiralOrder([*zip(*matrix)][::-1])