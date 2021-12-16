# https://leetcode.com/problems/permutations-ii/

class Solution:
    """
    Runtime: 215 ms, faster than 22.68% of Python3 online submissions for Permutations II.
    Memory Usage: 19.6 MB, less than 5.03% of Python3 online submissions for Permutations II.
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(functools.reduce(
            lambda P, n: [p[:i] + (n,) + p[i:] for p in P for i in range(len(p)+1)],
            nums,
            [()]
        ))

    """
    Runtime: 87 ms, faster than 34.78% of Python3 online submissions for Permutations II.
    Memory Usage: 14.5 MB, less than 64.94% of Python3 online submissions for Permutations II.
    https://leetcode.com/problems/permutations-ii/discuss/18616/6-lines-Python-Ruby
    """
    def permuteUnique(self, nums):
        return reduce(lambda perms, n: [p[:i] + [n] + p[i:]
                                        for p in perms
                                        for i in range((p + [n]).index(n) + 1)],
                      nums, [[]])

    """
    Runtime: 60 ms, faster than 70.08% of Python3 online submissions for Permutations II.
    Memory Usage: 14.3 MB, less than 91.84% of Python3 online submissions for Permutations II.
    https://leetcode.com/problems/permutations-ii/discuss/18649/Python-easy-to-understand-backtracking-solution.
    """
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
