class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        jumps = len(words[0])
        wordLen = jumps * len(words)

        if len(s) < wordLen:
            return []
        count1 = Counter(words)
        res = []

        for i in range(len(s) - wordLen + 1):
            substring = s[i:i + wordLen]
            count2 = Counter()
            for j in range(0, len(substring), jumps):
                word = substring[j: j + jumps]
                count2[word] +=1
        
            if count1 == count2:
                res.append(i)
        return res