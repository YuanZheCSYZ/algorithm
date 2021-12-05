# 661 https://leetcode.com/problems/image-smoother/

class Solution:
    """
    Runtime: 636 ms, faster than 81.08% of Python3 online submissions for Image Smoother.
    Memory Usage: 15.2 MB, less than 11.26% of Python3 online submissions for Image Smoother.
    """
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])
        res = [[0] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                y_min = max(0, y - 1)
                y_max = min(y + 1, m - 1)
                x_min = max(0, x - 1)
                x_max = min(x + 1, n - 1)

                s = 0
                cnt = 0
                for j in range(y_min, y_max + 1):
                    for i in range(x_min, x_max + 1):
                        cnt += 1
                        s += img[j][i]

                res[y][x] = s // cnt

        return res

    """
    Runtime: 560 ms, faster than 90.77% of Python3 online submissions for Image Smoother.
    Memory Usage: 15.1 MB, less than 35.59% of Python3 online submissions for Image Smoother.
    """
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])
        res = [[0] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                y_min = max(0, y - 1)
                y_max = min(y + 1, m - 1)
                x_min = max(0, x - 1)
                x_max = min(x + 1, n - 1)

                s = 0
                for j in range(y_min, y_max + 1):
                    s += sum(img[j][x_min:x_max + 1])

                res[y][x] = s // ((x_max + 1 - x_min) * ((y_max + 1 - y_min)))

        return res

    """
    Runtime: 544 ms, faster than 90.99% of Python3 online submissions for Image Smoother.
    Memory Usage: 14.9 MB, less than 58.11% of Python3 online submissions for Image Smoother.
    """
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])
        res = [[0] * n for _ in range(m)]
        for y, x in [(y, x) for y in [0, m - 1] for x in range(n)] + [(y, x) for y in range(1, m - 1) for x in
                                                                      [0, n - 1]]:
            y_min = max(0, y - 1)
            y_max = min(y + 1, m - 1)
            x_min = max(0, x - 1)
            x_max = min(x + 1, n - 1)

            s = 0
            for j in range(y_min, y_max + 1):
                s += sum(img[j][x_min:x_max + 1])

            res[y][x] = s // ((x_max + 1 - x_min) * ((y_max + 1 - y_min)))

        for y in range(1, m - 1):
            for x in range(1, n - 1):
                s = 0
                for j in range(y - 1, y + 2):
                    s += sum(img[j][x - 1:x + 2])

                res[y][x] = s // 9

        return res
