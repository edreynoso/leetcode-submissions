import heapq

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = {i:[] for i in range(1, n+1)}

        for a, b, distance in roads:

            graph[a].append((b, distance))
            graph[b].append((a, distance))


        paths = []
        
        q = collections.deque()

        q.append(1)

        seen = set()
        seen.add(1)

        ans = float("inf")

        while q:

            node = q.popleft()

            connections = graph.get(node)

            for v, w in connections:

                ans = min(ans, w)

                if v not in seen:

                    seen.add(v)
                    q.append(v)

        return ans

            