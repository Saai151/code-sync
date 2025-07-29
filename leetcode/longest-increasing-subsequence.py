class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = [1] * len(nums)

        for i in range(len(nums)):
            subproblems = [l[k] for k in range(i) if nums[k] < nums[i]]
            l[i] = max(subproblems, default=0) + 1
        
        return max(l)