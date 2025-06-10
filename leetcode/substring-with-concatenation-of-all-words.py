class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        length = len(words[0])
        count = Counter(words)
        res = []
        
        
        for i in range(0, len(s) - length + 1):
            substring = s[i: i + length*len(words)]
            listSubstring = []
            
            for j in range(0, len(substring), length):
                listSubstring.append(substring[j:j+length])

            count2 = Counter(listSubstring)
            num = 0
            for word in words:
                if word in substring and count[word] == count2[word]:
                    num +=1
                    if num == len(words):
                        res.append(i)
        return res