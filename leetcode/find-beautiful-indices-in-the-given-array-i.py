class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        result = []
        len1 = len(a)
        len2 = len(b)

        indexA = []
        indexB = []


        for i in range(len(s)):
            substring_a = s[i: i + len1]
            substring_b = s[i: i + len2]
            
            if substring_a == a:
                indexA.append(i)
            if substring_b == b:
                indexB.append(i)

        print(indexA)
        print(indexB)
        j = 0
        for i in indexA:
            while (j < len(indexB) and indexB[j] < i - k):
                j +=1

            if (j < len(indexB) and indexB[j] <= k + i):
                result.append(i)
            
        
        return result