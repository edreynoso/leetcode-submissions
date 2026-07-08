class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1

        count = 0

        for num in nums:

            if num == 0:
                count +=1
                continue

            product *= num

        output = [0] * len(nums)

        if count >= 2:
            return output

        for i in range(len(nums)):

            if nums[i] == 0:
                output[i] = product
                continue

            if count == 0:
                output[i] = product // nums[i]

            else:
                output[i] = 0

        return output