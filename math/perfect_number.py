# 507 https://leetcode.com/problems/perfect-number/
class Solution(object):
    """
    Runtime: 24 ms, faster than 78.50% of Python online submissions for Perfect Number.
    Memory Usage: 13.2 MB, less than 100.00% of Python online submissions for Perfect Number.
    """
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 1:
            return False

        sum_d = 1
        right = int(math.sqrt(num))
        left = 2
        while left <= right:
            if num % left == 0:
                tmp = num // left
                sum_d += tmp
                if tmp != left:
                    sum_d += left

                if tmp < right:
                    right = tmp - 1

                if num < sum_d:
                    return False

            left += 1

        return num == sum_d


if __name__ == "__main__":
    Solution().checkPerfectNumber(28)
