# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        
        graph = {}

        def create_graph(root):

            if not root:
                return

            if root.left:
                graph[root.left] = root
            
            if root.right:
                graph[root.right] = root
            
            create_graph(root.right)
            create_graph(root.left)

        create_graph(root)

        q = collections.deque()

        q.append(target)

        seen = set()

        distance = 0

        res = []

        while q:

            for _ in range(len(q)):

                node = q.popleft()

                if distance == k:
                    res.append(node.val)
                    continue
                else:

                    if node.left and node.left not in seen:
                        q.append(node.left)
                    
                    if node.right and node.right not in seen:
                        q.append(node.right)

                    if node in graph and graph.get(node) not in seen:
                        q.append(graph.get(node))

                seen.add(node) 
            distance +=1 

        return res