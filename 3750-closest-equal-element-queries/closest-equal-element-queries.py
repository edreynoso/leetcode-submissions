class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)
        
        indicies = defaultdict(list)
        pos = [0] * n

        for i, num in enumerate(nums):

            pos[i] = len(indicies[num])

            indicies[num].append(i) 

        ans = []

        for q in queries:

            target = nums[q]

            arr = indicies.get(target)
            m = len(arr)

            if m == 1:
                ans.append(-1)

            else:

                next = pos[q]

                left = arr[((next - 1) % m)]
                right = arr[((next + 1) % m)]

                left_distance = abs(left - q)
                right_distance = abs(right - q)

                min_distance = min( left_distance, n - left_distance, right_distance, n - right_distance)

                ans.append(min_distance)
                
        return ans

                


            

