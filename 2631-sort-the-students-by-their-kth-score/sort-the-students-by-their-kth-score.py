import heapq

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        pq = []
        
        heapq.heapify(pq)

        for student in score:

            heapq.heappush(pq, (-student[k], student))

        ans = []

        while pq: 
            ans.append(heapq.heappop(pq)[1])

        return ans