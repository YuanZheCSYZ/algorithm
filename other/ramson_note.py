# 383 https://leetcode.com/problems/ransom-note/submissions/

class Solution(object):
    """
    Runtime: 68 ms, faster than 60.98% of Python online submissions for Ransom Note.
    Memory Usage: 13.4 MB, less than 97.65% of Python online submissions for Ransom Note.
    """
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt_a = {}
        for x in ransomNote:
            if x not in cnt_a:
                cnt_a[x] = 1
            else:
                cnt_a[x] += 1

        cnt_b = {}
        for x in magazine:
            if x not in cnt_a:
                continue
            if x not in cnt_b:
                cnt_b[x] = 1
            else:
                cnt_b[x] += 1

        for x in cnt_a:
            if x not in cnt_b or cnt_b[x] < cnt_a[x]:
                return False

        return True

    """
    Runtime: 104 ms, faster than 31.96% of Python online submissions for Ransom Note.
    Memory Usage: 13.6 MB, less than 83.53% of Python online submissions for Ransom Note.
    """
    def canConstruct(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

    """
    Runtime: 24 ms, faster than 98.04% of Python online submissions for Ransom Note.
    Memory Usage: 13.7 MB, less than 65.10% of Python online submissions for Ransom Note.
    https://leetcode.com/problems/ransom-note/discuss/573185/Runtime%3A-100-or-One-Line-Python3
    """
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(letter) <= magazine.count(letter) for letter in set(ransomNote))