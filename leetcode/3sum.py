class Solution:
    def twoSum(self, arr, start, target):
        left = start
        right = len(arr) - 1
        pairs = []
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:  
                pairs.append([arr[left], arr[right]])
                
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
        return pairs
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
            
        nums.sort() 
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            if nums[i] > 0:
                break
                
            target = -nums[i]
            pairs = self.twoSum(nums, i + 1, target)
            
            for pair in pairs:
                result.append([nums[i]] + pair)
        
        return result