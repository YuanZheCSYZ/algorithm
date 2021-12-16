# https://leetcode.com/problems/4sum/submissions/

class Solution:
    """
    Runtime: 80 ms, faster than 99.08% of Python3 online submissions for 4Sum.
    Memory Usage: 14.2 MB, less than 78.84% of Python3 online submissions for 4Sum.
    """
    def fourSum(self, nums: List[int], target: int, sorting=False, N=4, res=None, results=None) -> List[List[int]]:
        if not sorting:
            nums.sort()
        if res is None:
            res = []
        if results is None:
            results = []

        n = len(nums)
        if n < N or N < 2:
            pass
        elif N == 2:
            l = 0
            r = n - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(res + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for x in range(0, n - N + 1):
                if target < nums[x] * N or nums[-1] * N < target:
                    break
                if x == 0 or nums[x - 1] != nums[x]:
                    self.fourSum(
                        nums[x + 1:],
                        target - nums[x],
                        True,
                        N - 1,
                        res + [nums[x]],
                        results)

        return results
