#

class Solution:
    """
    Time Limit Exceeded
    """
    def canPartition(self, nums: List[int], target=None) -> bool:
        if not nums:
            return not target

        if target is None:
            return self.canPartition(nums[1:], nums[0])

        return self.canPartition(nums[1:], target - nums[0]) or self.canPartition(nums[1:], target + nums[0])

    """
    Runtime: 3892 ms, faster than 12.43% of Python3 online submissions for Partition Equal Subset Sum.
    Memory Usage: 15 MB, less than 66.00% of Python3 online submissions for Partition Equal Subset Sum.
    """
    def canPartition(self, nums: List[int]) -> bool:
        base = {nums[0]}
        for x in nums[1:]:
            tmp = set()
            for y in base:
                tmp.update({x + y, x - y, y - x})

            base = tmp

        return 0 in base

    """
    Runtime: 748 ms, faster than 68.91% of Python3 online submissions for Partition Equal Subset Sum.
    Memory Usage: 14.5 MB, less than 82.50% of Python3 online submissions for Partition Equal Subset Sum.
    """
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False

        target = s // 2
        dp = [True] + [False for _ in range(target)]
        for x in nums:
            if target < x:
                return False

            for y in range(target, x, -1):
                dp[y] |= dp[y - x]

            dp[x] = True
            if dp[target]:
                break

        return dp[target]

    """
    Runtime: 108 ms, faster than 94.99% of Python3 online submissions for Partition Equal Subset Sum.
    Memory Usage: 14.7 MB, less than 69.57% of Python3 online submissions for Partition Equal Subset Sum.
    https://leetcode.com/problems/partition-equal-subset-sum/discuss/276278/Python-DP-and-(DFS%2BMemo)
    """
    def canPartition(self, nums):
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1:
            return False
        nums.sort(reverse=True)

        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j + 1, x - nums[j]):
                            memo[x] = True
                            break
            return memo[x]

        return dfs(0, s >> 1)
