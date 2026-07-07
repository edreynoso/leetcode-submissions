class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        num = str(n)

        res = []

        total = 0

        for c in num:

            if int(c) > 0:
                res.append(c)
                total += int(c)

        if len(res) == 0:
            return 0
        
        res = int("".join(res))

        return res * total

        