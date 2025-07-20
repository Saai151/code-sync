from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        window = SortedList()

        for i, num in enumerate(nums):
            # Find smallest number >= num - valueDiff
            pos = window.bisect_left(num - valueDiff)

            # Check if there's any number within valueDiff
            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True

            window.add(num)

            # Maintain sliding window of size indexDiff
            if i >= indexDiff:
                window.remove(nums[i - indexDiff])

        return False