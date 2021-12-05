# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    """
    Runtime: 48 ms, faster than 98.32% of Python3 online submissions for Min Cost Climbing Stairs.
    Memory Usage: 14.6 MB, less than 24.35% of Python3 online submissions for Min Cost Climbing Stairs.
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mapping = {
            -1: 0,
            0: cost[0]
        }
        n = len(cost)
        for i in range(1, n):
            mapping[i] = min(mapping[i - 1], mapping[i - 2]) + cost[i]

        return min(mapping[n - 1], mapping[n - 2])
