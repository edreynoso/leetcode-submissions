class Solution:
    def partitionString(self, s: str) -> int:

        if not s:
            return 0

        if len(s) == 1:
            return 1
        
        partitions = []

        l = 0
        r = l

        window = set()

        while l  <= r and r < len(s):

            if s[r] not in window:

                window.add(s[r])
                r +=1
            
            else:

                l = r
                partitions.append(window)
                window = set()
        
        partitions.append(window)
        
        return len(partitions)
            