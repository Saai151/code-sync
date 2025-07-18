class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        idx1, idx2 = -1, -1
        dist = float('inf')

        for i, word in enumerate(wordsDict):
            if word == word1:
                if word1 == word2:
                    idx1 = idx2
                    idx2 = i
                else:
                    idx1 = i
            elif word == word2:
                idx2 = i
            
            if idx1 != -1 and idx2 != -1 and idx1 != idx2:
                dist = min(dist, abs(idx1 - idx2))
        
        return dist