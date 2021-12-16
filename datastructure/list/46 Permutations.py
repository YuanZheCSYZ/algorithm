# https://leetcode.com/problems/permutations/

class Solution:
    """
    Runtime: 44 ms, faster than 42.24% of Python3 online submissions for Permutations.
    Memory Usage: 14.6 MB, less than 15.66% of Python3 online submissions for Permutations.
    """
    def permute(self, nums: List[int], picked=None) -> List[List[int]]:
        if picked is None:
            picked = []
        elif len(nums) == len(picked):
            return [()]

        res = []
        for x in nums:
            if x not in picked:
                picked.append(x)
                res.extend([y + (x,) for y in self.permute(nums, picked)])
                picked.pop()

        return res

    """
    Runtime: 24 ms, faster than 99.95% of Python3 online submissions for Permutations.
    Memory Usage: 14.6 MB, less than 15.66% of Python3 online submissions for Permutations.
    https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        return functools.reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p)+1)],
                  nums, [[]])