class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)
        
        indicies = {num: [] for num in nums}

        for i, num in enumerate(nums):

            indicies[num].append(i) 

        ans = []

        for q in queries:

            target = nums[q]

            if len(indicies[target]) == 1:
                ans.append(-1)

            else:

                arr = indicies.get(target)

                m = len(arr)

                next = bisect_left(arr, q)

                left = arr[((next - 1) % m)]
                right = arr[((next + 1) % m)]

                left_distance = abs(left - q)
                right_distance = abs(right - q)

                min_distance = min( left_distance, n - left_distance, right_distance, n - right_distance)

                ans.append(min_distance)
                
        return ans

                


            

