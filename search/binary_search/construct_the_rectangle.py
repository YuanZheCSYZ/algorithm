# 492 https://leetcode.com/problems/construct-the-rectangle/

class Solution(object):
    """
    Runtime: 16 ms, faster than 89.61% of Python online submissions for Construct the Rectangle.
    Memory Usage: 13.4 MB, less than 51.30% of Python online submissions for Construct the Rectangle.
    """
    def constructRectangle(self, area):
        mid = int(math.sqrt(area))
        if mid * mid == area:
            return [mid, mid]

        L = area
        W = 1
        while W < mid:
            if area % mid == 0:
                W = mid
                L = area // mid
                break

            mid -= 1

        return [L, W]

    """
    Runtime: 12 ms, faster than 98.70% of Python online submissions for Construct the Rectangle.
    Memory Usage: 13.5 MB, less than 31.17% of Python online submissions for Construct the Rectangle.
    """
    def constructRectangle(self, area):
        mid = int(math.sqrt(area))
        while area % mid:
            mid -= 1

        return [area // mid, mid]