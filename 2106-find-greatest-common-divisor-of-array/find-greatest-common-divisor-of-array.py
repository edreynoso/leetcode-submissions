import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        min_num = float("inf")

        max_num = 0

        for num in nums:

            min_num = min(min_num, num)

            max_num = max(max_num, num)

        return math.gcd(max_num, min_num)