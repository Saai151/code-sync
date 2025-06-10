class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        
        curr = 0
        length = math.inf

        left = 0

        for right in range(len(nums)):
            if curr < target:
                curr += nums[right]
            while(curr >= target):
                length = min(length, right - left + 1)
                curr -= nums[left]
                left +=1
        
        if sum(nums) < target:
            return 0
        return length