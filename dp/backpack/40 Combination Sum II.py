# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    """
    Runtime: 416 ms, faster than 5.12% of Python3 online submissions for Combination Sum II.
    Memory Usage: 14.5 MB, less than 20.98% of Python3 online submissions for Combination Sum II.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [set() for _ in range(target + 1)]
        for c in candidates:
            if target < c:
                continue

            dp_c = copy.deepcopy(dp)
            c_s = str(c)
            dp_c[c].add(c_s)
            for x in range(1, target + 1):
                if x + c <= target:
                    dp_c[x + c].update({y + "," + c_s for y in dp[x]})

            dp = dp_c

        return [[int(y) for y in x.split(",")] for x in dp[target]]

    """
    Runtime: 48 ms, faster than 83.42% of Python3 online submissions for Combination Sum II.
    Memory Usage: 14.1 MB, less than 92.61% of Python3 online submissions for Combination Sum II.
    https://leetcode.com/problems/combination-sum-ii/discuss/16870/DP-solution-in-Python
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [set() for _ in range(target + 1)]
        for c in candidates:
            if target < c:
                continue

            for x in range(target - c, 0, -1):
                dp[x + c] |= {y + (c,) for y in dp[x]}

            dp[c].add((c,))

        return dp[target]
