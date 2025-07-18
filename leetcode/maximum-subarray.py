class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = float('-inf')
        maxSum = float('-inf')
        for i in range(len(nums)):
            print(currSum, nums[i])
            if currSum + nums[i] < nums[i]:
                currSum = nums[i]
            else:
                currSum += nums[i]
            maxSum = max(currSum, maxSum)


        return maxSum