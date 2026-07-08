class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()

        char_arr = list(s)

        digits = set()

        for i in range(10):

            digits.add(str(i))


        def convert(arr):

            sign = {"-": -1, "+": 1}

            number = ""

            isNegative = 1

            prev = ""

            for digit in arr:

                if prev not in digits and digit not in digits and len(prev) > 0:
                    break

                if digit in sign and len(number) == 0:
                    isNegative = sign[digit]
                    prev = digit
                    continue
                
                if digit == "0" and len(number) == 0 and isNegative < 0:
                    prev = digit
                    continue
                
                if digit not in digits:
                    break

                number += digit

                prev = digit

            return isNegative * int(number) if len(number) > 0 else 0

        number = convert(char_arr)

        if number < -(2 ** 31):
            return -(2**31)

        if number > 2** 31 -1:
            return 2 **31 -1

        return number