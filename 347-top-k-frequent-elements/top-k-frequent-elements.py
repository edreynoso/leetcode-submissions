class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {num: 0 for num in nums}

        for num in nums: 

            freq[num] += 1

        freq_list = list(freq.items())

        freq_list.sort(key = lambda x: x[1], reverse = True)

        res = []

        for i in range(k):

            res.append(freq_list[i][0])

        return res