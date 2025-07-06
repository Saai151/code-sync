class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in index:
                return [index[complement], i]
            else:
                index[nums[i]] = i