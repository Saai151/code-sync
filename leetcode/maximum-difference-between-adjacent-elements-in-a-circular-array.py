class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxAdjacent = abs(nums[0] - nums[len(nums) - 1])

        for i in range(len(nums) - 1):
            diff = abs(nums[i] - nums[i + 1])
            print(diff)
            maxAdjacent = max(diff, maxAdjacent)

        return maxAdjacent