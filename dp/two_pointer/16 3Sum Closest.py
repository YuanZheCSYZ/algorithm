# https://leetcode.com/problems/3sum-closest/
class Solution:
    """
    Runtime: 188 ms, faster than 38.93% of Python3 online submissions for 3Sum Closest.
    Memory Usage: 14.5 MB, less than 11.72% of Python3 online submissions for 3Sum Closest.
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        m = sum(nums[:3])
        n = len(nums)
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = target - s
                if diff == 0:
                    return s

                if abs(diff) < abs(target - m):
                    m = s

                if diff < 0:
                    r -= 1
                else:
                    l += 1

        return m
