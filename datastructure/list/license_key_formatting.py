# 482 https://leetcode.com/problems/license-key-formatting/

class Solution(object):
    """
    Runtime: 448 ms, faster than 48.38% of Python online submissions for License Key Formatting.
    Memory Usage: 15.8 MB, less than 34.41% of Python online submissions for License Key Formatting.
    """
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()
        remaining = len(s) % k
        res = s[:remaining]
        for x in range(len(s) // k):
            if res:
                res += "-"

            res += s[remaining + k * x: remaining + k * x + k]

        return res

    """
    Runtime: 20 ms, faster than 98.92% of Python online submissions for License Key Formatting.
    Memory Usage: 15.3 MB, less than 68.82% of Python online submissions for License Key Formatting.
    """
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()
        remaining = len(s) % k

        res = []
        if remaining:
            res.append(s[:remaining])

        for x in range(len(s) // k):
            res.append(s[remaining + k * x: remaining + k * x + k])

        return "-".join(res)

    """
    Runtime: 24 ms, faster than 93.98% of Python online submissions for License Key Formatting.
    Memory Usage: 15.9 MB, less than 27.31% of Python online submissions for License Key Formatting.
    https://leetcode.com/problems/license-key-formatting/discuss/131978/beats-100-python3-submission
    """
    def licenseKeyFormatting(self, S, K):
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i + K] for i in range(0, len(S), K))[::-1]
