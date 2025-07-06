class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        freq1 = Counter(s)
        freq2 = Counter(t)



        for char in t:
            if freq1[char] != freq2[char]:
                return False
        return True