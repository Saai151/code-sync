class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        right = len(matrix)
        left = 0

        while(left < right):
            mid = (left + right) //2

            result = self.search(matrix[mid], target)

            if result == target:
                return True
            if result == -1:
                left = mid + 1
            else:
                right = mid
        return False

    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)
        left = 0

        while(left < right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return target
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        if target > nums[-1]:
            return -1
        else:
            return -2