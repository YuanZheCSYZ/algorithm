# 500 https://leetcode.com/problems/keyboard-row/

class Solution(object):
    """
    Runtime: 17 ms, faster than 45.62% of Python online submissions for Keyboard Row.
    Memory Usage: 13.5 MB, less than 42.40% of Python online submissions for Keyboard Row.
    """
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_sets = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        return [x for x in words for row in row_sets if row.issuperset(set(x.lower()))]

    """
    Runtime: 20 ms, faster than 44.70% of Python online submissions for Keyboard Row.
    Memory Usage: 13.2 MB, less than 98.16% of Python online submissions for Keyboard Row.
    """
    def findWords(self, words):
        row_sets = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        res =[]
        for x in words:
            for row in row_sets:
                if set(x.lower()) <= row:
                    res.append(x)
                    break
        return res

    """
    Runtime: 10 ms, faster than 94.01% of Python online submissions for Keyboard Row.
    Memory Usage: 13.5 MB, less than 68.20% of Python online submissions for Keyboard Row.
    """
    def findWords(self, words):
        row_sets = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        return [x for x in words for row in row_sets if set(x.lower()) <= row]


    """
    Runtime: 20 ms, faster than 44.70% of Python online submissions for Keyboard Row.
    Memory Usage: 13.6 MB, less than 11.52% of Python online submissions for Keyboard Row.
    https://leetcode.com/problems/keyboard-row/discuss/97888/Regex-one-liner-Ruby-%2B-Python
    """
    def findWords(self, words):
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
