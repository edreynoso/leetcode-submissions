class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        if not s:
            return 0

        MAX = 2 ** 31 -1
        MIN = -(2**31)

        idx = 0
        number = 0

        sign = 1

        if s[idx] == "-":
            sign = -1
            idx +=1
        elif s[idx] == "+":
            idx +=1

        while (idx < len(s) and s[idx].isdigit()):

            number = number * 10 + int(s[idx]) 
            idx +=1

        
        number *= sign

        if number < MIN:
            return MIN

        if number > MAX:
            return MAX

        return number
        