# 70 https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    """
    Runtime: 32 ms, faster than 61.72% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 14.2 MB, less than 72.58% of Python3 online submissions for Climbing Stairs.
    """
    def climbStairs(self, n: int) -> int:
        return self.permutations(n, {1: 1, 2: 2})

    def permutations(self, n, existing_solution_dict):
        if n <= 0:
            return 0
        elif n in existing_solution_dict:
            return existing_solution_dict[n]
        else:
            existing_solution_dict[n] = self.permutations(n - 1, existing_solution_dict) + self.permutations(n - 2,
                                                                                                             existing_solution_dict)

        return existing_solution_dict[n]

    """
    Runtime: 28 ms, faster than 83.88% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 13.9 MB, less than 98.13% of Python3 online submissions for Climbing Stairs.
    """
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first, second = 1, 2

        for i in range(3, n + 1):
            first, second = second, second + first

        return second