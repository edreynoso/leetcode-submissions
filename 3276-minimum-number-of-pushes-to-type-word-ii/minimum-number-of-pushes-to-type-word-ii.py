class Solution:
    def minimumPushes(self, word: str) -> int:
        
        mapped_chars = {c:0 for c in word}

        for c in word:

            mapped_chars[c] += 1


        chars = list(mapped_chars.values())

        chars.sort(reverse=True)

        total = 0

        for i, c in enumerate(chars):

            total += ((i//8) + 1) * c

        return total


