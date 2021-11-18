# 58 https://leetcode.com/problems/length-of-last-word/submissions/
class Solution:
    """
    Runtime: 32 ms, faster than 60.95% of Python3 online submissions for Length of Last Word.
    Memory Usage: 14 MB, less than 96.72% of Python3 online submissions for Length of Last Word.
    """
    def lengthOfLastWord(self, s: str) -> int:
        sub_s = s.strip().split(" ")
        if sub_s:
            return len(sub_s[-1])
        else:
            return 0

    """
    Runtime: 32 ms, faster than 60.95% of Python3 online submissions for Length of Last Word.
    Memory Usage: 14.2 MB, less than 65.08% of Python3 online submissions for Length of Last Word.
    """
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for x in s[::-1]:
            if x == " ":
                if cnt:
                    return cnt

                continue
            else:
                cnt += 1

        return cnt

    """
    Runtime: 28 ms, faster than 83.95% of Python3 online submissions for Length of Last Word.
    Memory Usage: 14.4 MB, less than 36.49% of Python3 online submissions for Length of Last Word.
    """
    def lengthOfLastWord(self, s: str) -> int:
        split_words_list = s.split()
        return len(split_words_list[-1])

    """
    Runtime: 28 ms, faster than 83.95% of Python3 online submissions for Length of Last Word.
    Memory Usage: 14.3 MB, less than 36.49% of Python3 online submissions for Length of Last Word.
    """
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for x in range(len(s)):
            if s[-x - 1] == " ":
                if cnt:
                    return cnt

                continue
            else:
                cnt += 1

        return cnt