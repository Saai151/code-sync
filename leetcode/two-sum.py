class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vis = {}
            

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in vis:
                return [i, vis[complement]]
            else:
                vis[nums[i]] = i