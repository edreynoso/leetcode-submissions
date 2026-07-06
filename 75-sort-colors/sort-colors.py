class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = {0: 0, 1: 0, 2: 0}

        for num in nums:

            count[num] +=1

        idx = 0

        for k,v in count.items():

            for i in range(v):

                nums[idx] = k
                idx +=1

        


