# 461 https://leetcode.com/problems/hamming-distance/

class Solution(object):
    """
    Runtime: 16 ms, faster than 74.32% of Python online submissions for Hamming Distance.
    Memory Usage: 13.3 MB, less than 66.26% of Python online submissions for Hamming Distance.
    """
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        cnt = 0
        while x != y:
            cnt += (x & 1) != (y & 1)
            x = x >> 1
            y = y >> 1

        return cnt

    """
    Runtime: 12 ms, faster than 96.20% of Python online submissions for Hamming Distance.
    Memory Usage: 13.3 MB, less than 90.27% of Python online submissions for Hamming Distance.
    https://leetcode.com/problems/hamming-distance/discuss/1585400/C%2B%2B-Two-Simple-and-Clean-Solutions-Explained-0ms-Faster-than-100
    """
    def hammingDistance(self, x, y):
        cnt = 0
        num = x ^ y
        while num:
            cnt += num & 1
            num >>= 1

        return cnt