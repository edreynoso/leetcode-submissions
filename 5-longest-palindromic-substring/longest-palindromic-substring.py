class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        if n ==1:
            return s


        max_len = 1
        res = s[0]

        for i in range(n):

            l = i -1
            r = i +1

            while l >= 0 and r < n and s[l] == s[r]:

                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    res = s[l:r+1]

                l -=1
                r +=1

            r = i + 1
            l = i

            while l >= 0 and r < n and s[l] == s[r]:

                if r - l + 1 > max_len:

                    max_len = r - l +1

                    res = s[l:r+1]

                l -=1
                r +=1

        return res 
            