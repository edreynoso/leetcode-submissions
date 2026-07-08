class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_x = 0
        
        for num in nums:

            if num-1 not in nums:
                
                x = num + 1

                while x in nums:
                    x +=1
                
                max_x = max(max_x, x - num)
        
        return max_x