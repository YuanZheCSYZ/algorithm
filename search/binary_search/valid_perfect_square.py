# 367 https://leetcode.com/problems/valid-perfect-square/

class Solution(object):
    """
    Runtime: 20 ms, faster than 55.25% of Python online submissions for Valid Perfect Square.
    Memory Usage: 13.4 MB, less than 35.08% of Python online submissions for Valid Perfect Square.
    """
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num < 0:
            return False
        elif num <= 1:
            return True

        left = 1
        right = num - 1
        while left <= right:
            mid = (left + right) // 2
            mid_square = mid * mid
            if num == mid_square:
                return True
            elif num < mid_square:
                right = mid - 1
            else:
                left = mid + 1

        return False

    """
    Runtime: 24 ms, faster than 30.51% of Python online submissions for Valid Perfect Square.
    Memory Usage: 13.5 MB, less than 11.19% of Python online submissions for Valid Perfect Square.
    https://leetcode.com/problems/valid-perfect-square/discuss/83874/A-square-number-is-1%2B3%2B5%2B7%2B...-JAVA-code
    """
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    """
    Runtime: 16 ms, faster than 81.69% of Python online submissions for Valid Perfect Square.
    Memory Usage: 13.5 MB, less than 11.19% of Python online submissions for Valid Perfect Square.
    https://leetcode.com/problems/valid-perfect-square/discuss/83874/A-square-number-is-1%2B3%2B5%2B7%2B...-JAVA-code
    """
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        x = num
        while x * x > num:
            x = (x + num / x) >> 1
        return x * x == num