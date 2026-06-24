import heapq
class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        scores_sorted = []

        heapq.heapify(scores_sorted)

        for i in range(len(score)):

            heapq.heappush(scores_sorted, (-score[i][k], score[i]))
        
        for i in range(len(score)):

            student = heapq.heappop(scores_sorted)

            student= student[1]

            score[i] = student

        return score

        