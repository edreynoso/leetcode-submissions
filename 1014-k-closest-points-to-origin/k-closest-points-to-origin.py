import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        def getDistance(x,y):

            return ((0 - x) ** 2) + ((0 - y) ** 2)

        distances = []

        heapq.heapify(distances)


        for i in range(len(points)):

            x, y = points[i][0], points[i][1]

            distance = getDistance(x,y)

            heapq.heappush(distances, (distance, i))

        res = []

        for i in range(k):

            point = heapq.heappop(distances)

            idx = point[1]

            res.append(points[idx])

        return res
        