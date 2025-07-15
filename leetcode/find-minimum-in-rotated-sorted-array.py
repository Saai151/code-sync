class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        #else the list has been rotated a number less than n

        left, right = 0, len(nums) -1
        res = float('inf')

        while(left<=right):
            if nums[left] <= nums[right]:
                res = min(nums[left], res)

            mid = (left + right) //2
           
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
        return res