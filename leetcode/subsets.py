class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        #[1,2,3]
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            #decition to not include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res