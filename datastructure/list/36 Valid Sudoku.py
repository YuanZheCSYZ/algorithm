# https://leetcode.com/problems/valid-sudoku/submissions/

class Solution:
    """
    Runtime: 92 ms, faster than 89.26% of Python3 online submissions for Valid Sudoku.
    Memory Usage: 14.3 MB, less than 43.57% of Python3 online submissions for Valid Sudoku.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty = "."
        n = 9
        nums_9 = [[[] for _ in range(3)] for _ in range(3)]
        for y in range(n):
            nums = list(filter(lambda num: num != empty, board[y]))
            if len(nums) != len(set(nums)):
                return False

            nums_v = []
            for x in range(n):
                if board[x][y] != empty:
                    nums_v.append(board[x][y])
                    nums_9[x // 3][y // 3].append(board[x][y])

                if x % 3 == 2 and y % 3 == 2:
                    if len(nums_9[x // 3][y // 3]) != len(set(nums_9[x // 3][y // 3])):
                        return False

            if len(nums_v) != len(set(nums_v)):
                return False

        return True