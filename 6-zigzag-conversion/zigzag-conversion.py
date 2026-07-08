class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or len(s) <= numRows:
            return s
        

        rows = [""] * numRows
        curr = 0
        direction = -1

        for c in s:

            rows[curr] += c

            if curr % (numRows -1) == 0:
                direction *= -1

            curr += direction

        return "".join(rows)