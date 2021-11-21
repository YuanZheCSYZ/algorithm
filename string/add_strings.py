# 415 https://leetcode.com/problems/add-strings

class Solution(object):

    """
    Runtime: 20 ms, faster than 93.45% of Python online submissions for Add Strings.
    Memory Usage: 14 MB, less than 11.51% of Python online submissions for Add Strings.
    """
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        res = []
        over = 0
        for x in range(-1, -len(num2) - 1, -1):
            tmp = int(num1[x]) + int(num2[x]) + over
            if tmp >= 10:
                over = 1
                tmp -= 10
            else:
                over = 0

            res.append(str(tmp))

        x = len(num1) - len(num2) - 1
        while over and x >= 0:
            tmp = int(num1[x]) + over
            if tmp >= 10:
                over = 1
                tmp -= 10
            else:
                over = 0

            res.append(str(tmp))
            x -= 1

        if over:
            res.append(str(over))
        elif x >= 0:
            res.append(num1[0:x + 1])

        return "".join(res[::-1])

    """
    Runtime: 24 ms, faster than 85.07% of Python online submissions for Add Strings.
    Memory Usage: 13.9 MB, less than 26.55% of Python online submissions for Add Strings.
    """
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        res = ""
        over = 0
        for x in range(-1, -len(num2) - 1, -1):
            tmp = int(num1[x]) + int(num2[x]) + over
            if tmp >= 10:
                over = 1
                tmp -= 10
            else:
                over = 0

            res += str(tmp)

        x = len(num1) - len(num2) - 1
        while over and x >= 0:
            tmp = int(num1[x]) + over
            if tmp >= 10:
                over = 1
                tmp -= 10
            else:
                over = 0

            res += str(tmp)
            x -= 1

        if over:
            res += str(over)
        elif x >= 0:
            # !!!!!
            res += num1[0:x + 1][::-1]

        return res[::-1]