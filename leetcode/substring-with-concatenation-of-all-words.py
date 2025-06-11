class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        jumps = len(words[0])
        wordLen = jumps * len(words)

        count1 = Counter(words)
        res = []

        for i in range(0, len(s)):
            substring = s[i:i + wordLen]
            count2 = Counter()
            for j in range(0, len(substring), jumps):
                word = substring[j: j + jumps]
                if word in count1 and word not in count2:
                    count2[word] = 1
                elif word in count1.keys():
                    count2[word] +=1
                else:
                    print('breaking')
                    break
            if count1 == count2:
                res.append(i)
        return res