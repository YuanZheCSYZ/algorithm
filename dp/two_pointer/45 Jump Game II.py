# https://leetcode.com/problems/jump-game-ii/

class Solution:
    """
    Runtime: 4580 ms, faster than 27.37% of Python3 online submissions for Jump Game II.
    Memory Usage: 15.5 MB, less than 13.54% of Python3 online submissions for Jump Game II.
    """
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] + [None for _ in range(n - 1)]
        for i, x in enumerate(nums[:-1]):
            for y in range(1, min(x + 1, n - i)):
                j = i + y
                s = 1 + dp[i]
                if dp[j] is None or s < dp[j]:
                    dp[j] = s

        return dp[-1]

    """
    Runtime: 179 ms, faster than 48.99% of Python3 online submissions for Jump Game II.
    Memory Usage: 15.1 MB, less than 73.26% of Python3 online submissions for Jump Game II.
    https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!
    """
    def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times

    """
    Runtime: 136 ms, faster than 56.23% of Python3 online submissions for Jump Game II.
    Memory Usage: 15.4 MB, less than 23.12% of Python3 online submissions for Jump Game II.
    https://leetcode.com/problems/jump-game-ii/discuss/1192401/Easy-Solutions-w-Explanation-or-Optimizations-from-Brute-Force-to-DP-to-Greedy-BFS
    
    Greedy
    """
    def jump(self, nums):
        step = 0
        i = 0
        rim = 0
        farthest = 0

        n = len(nums)
        while rim < n - 1:
            farthest = max(farthest, i + nums[i])
            if i == rim:
                step += 1
                rim = farthest
                if n - 1 <= farthest:
                    break

            i += 1

        return step
