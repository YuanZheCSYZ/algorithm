# https://leetcode.com/problems/combination-sum/

class Solution:
    """
    Runtime: 56 ms, faster than 89.58% of Python3 online submissions for Combination Sum.
    Memory Usage: 14.7 MB, less than 7.36% of Python3 online submissions for Combination Sum.

    Backpack: unlimited size and usage.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for x in candidates:
            for i in range(0, target-x+1):
                dp[i + x].extend([c + [x] for c in dp[i]])

        return dp[-1]

    """
    Runtime: 48 ms, faster than 97.74% of Python3 online submissions for Combination Sum.
    Memory Usage: 14.3 MB, less than 52.72% of Python3 online submissions for Combination Sum.
    https://leetcode.com/problems/combination-sum/discuss/481569/Python3-backtracking-and-dp
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def fn(i, x):
            """Populate ans via backtracking."""
            if x == 0: return ans.append(stack.copy())  # store a copy
            for ii in range(i, len(candidates)):
                if x < candidates[ii]: break
                stack.append(candidates[ii])
                fn(ii, x - candidates[ii])
                stack.pop()

        ans, stack = [], []
        fn(0, target)
        return ans