class Solution:
    def search(self, nums: List[int], target: int) -> int:


        right = len(nums)
        left = 0

        while(left < right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        return -1