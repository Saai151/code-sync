class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        left = 0

        curr = ""
        for right in range(len(s)):
            while(s[right] in curr):
                left +=1
                curr = s[left: right]
            curr += s[right]
            print(curr)
            max_len = max(len(curr), max_len)
        
        return max_len