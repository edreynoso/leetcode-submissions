class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))

        count = 0

        r = 0

        for start, end in intervals:

            if end > r:
                count +=1 
                r = end

        return count