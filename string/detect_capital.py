# 520 https://leetcode.com/problems/detect-capital/submissions/

class Solution(object):
    """
    Runtime: 16 ms, faster than 85.45% of Python online submissions for Detect Capital.
    Memory Usage: 13.6 MB, less than 27.73% of Python online submissions for Detect Capital.
    """
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word == word.upper() or word == word.lower() or word[1:] == word[1:].lower()

    """
    Runtime: 12 ms, faster than 95.45% of Python online submissions for Detect Capital.
    Memory Usage: 13.6 MB, less than 27.73% of Python online submissions for Detect Capital.
    """
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word == word.upper() or word[1:] == word[1:].lower()

    """
    Runtime: 12 ms, faster than 95.45% of Python online submissions for Detect Capital.
    Memory Usage: 13.6 MB, less than 27.73% of Python online submissions for Detect Capital.
    https://leetcode.com/problems/detect-capital/discuss/99249/Python-has-useful-methods...
    """
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()