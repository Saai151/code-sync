class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        words = {word1: None, word2: None}
        dist = float('inf')

        if word1 == word2:
            indices = []
            for i in range(len(wordsDict)):
                word = wordsDict[i]
                if word == word1:
                    indices.append(i)
            
            for i in range(len(indices) - 1):
                diff = indices[i + 1] - indices[i]
                dist = min(dist, diff)

            return dist

        for i in range(len(wordsDict)):
            word = wordsDict[i]

            if word in words:
                words[word] = i
                if words[word1] != None and words[word2] != None:
                    print("calculating distance")
                    dist = min(dist, abs(words[word1] - words[word2]))
        
        print(words)
        return dist