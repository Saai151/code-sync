class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

       

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        z1 = nums1.count(0)
        z2 = nums2.count(0)

        sum1 += z1
        sum2 += z2
        if sum1 == sum2: return sum1

        if ((sum1 > sum2 and z2 == 0)
            or sum2 > sum1 and z1 == 0):
            return -1
        
        return max(sum1, sum2)