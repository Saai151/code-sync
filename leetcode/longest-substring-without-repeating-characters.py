class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, maxLen = 0, 0
        substring = ""

        for right in range(len(s)):
            curr = s[right]
            
            while curr in substring:
                left += 1
                substring = s[left: right]
            substring += s[right]

            maxLen = max(maxLen, len(substring))
        
        return maxLen