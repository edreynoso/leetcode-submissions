class Solution:
    def smallestPalindrome(self, s: str) -> str:

        if len(s) ==1:
            return s
        
        m = len(s) // 2

        if len(s) % 2 > 0:

            chars = [s[c] for c in range(m)]

            chars.sort()
            
            ans = "".join(chars)

            ans += s[m] + ans[::-1]

        else:

            chars = [s[c] for c in range(m)]

            chars.sort()

            ans = "".join(chars)

            ans += ans[::-1]

        return ans