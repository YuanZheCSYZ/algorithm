# https://leetcode.com/problems/container-with-most-water/

class Solution:
    """
    Runtime: 684 ms, faster than 91.39% of Python3 online submissions for Container With Most Water.
    Memory Usage: 27.5 MB, less than 75.58% of Python3 online submissions for Container With Most Water.

    heading towards the high bar
    """
    def maxArea(self, height: List[int]) -> int:
        m = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                m = max(m, (r-l) * height[l])
                l += 1
            else:
                m = max(m, (r-l) * height[r])
                r -= 1

        return m
