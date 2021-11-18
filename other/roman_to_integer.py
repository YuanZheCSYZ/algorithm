# 13 https://leetcode.com/problems/roman-to-integer/submissions/
class Solution:
    """
    Runtime: 36 ms, faster than 98.36% of Python3 online submissions for Roman to Integer.
    Memory Usage: 14.1 MB, less than 84.11% of Python3 online submissions for Roman to Integer.
    """
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        tmp = 0
        for x in s:
            num = mapping[x]
            if not tmp:
                tmp = num
                continue

            if num > tmp:
                result += num - tmp
                tmp = 0
            else:
                result += tmp
                tmp = num

        return result + tmp

    """
    Runtime: 32 ms, faster than 85.66% of Python3 online submissions for Roman to Integer.
    Memory Usage: 14 MB, less than 95.29% of Python3 online submissions for Roman to Integer.
    """
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        for index in range(len(s) - 1):
            num = mapping[s[index]]
            num_next = mapping[s[index + 1]]
            if num >= num_next:
                result += num
            else:
                result -= num

        return result + mapping[s[-1]]

    """
    Runtime: 44 ms, faster than 85.66% of Python3 online submissions for Roman to Integer.
    Memory Usage: 14.1 MB, less than 95.29% of Python3 online submissions for Roman to Integer.
    """
    def romanToInt(self, s: str) -> int:
        def getValue(x: str):
            if x == "I": return 1
            if x == "V": return 5
            if x == "X": return 10
            if x == "L": return 50
            if x == "C": return 100
            if x == "D": return 500
            if x == "M": return 1000

        result = 0
        for index in range(len(s) - 1):
            num = getValue(s[index])
            num_next = getValue(s[index + 1])
            if num >= num_next:
                result += num
            else:
                result -= num

        return result + getValue(s[-1])

