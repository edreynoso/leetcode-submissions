import heapq
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        res = []

        for i in range(len(searchWord)):

            search = searchWord[:i+1]

            results = []

            heapq.heapify(results)

            for product in products:

                if product.startswith(search):
                    heapq.heappush(results, product)
            
            
            level = []
            for i in range(3):

                if results:
                    level.append(heapq.heappop(results))

            res.append(level)

        return res




        