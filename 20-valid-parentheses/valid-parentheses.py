class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False
        
        close = {"(": ")", "{": "}", "[":"]"}

        stack = collections.deque()

        for c in s:

            if c in close:
                stack.append(c)
            else:

                if not stack:
                    return False
                open = stack.pop()

                if not close.get(open) == c:
                    return False

        return True if not stack else False