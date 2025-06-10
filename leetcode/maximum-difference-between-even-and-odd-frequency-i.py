class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = Counter(s)

        maxOdd = -math.inf
        minEven = math.inf

        for i in hashmap:
            print(i, hashmap[i])
            if hashmap[i] % 2 == 0:
                minEven = min(hashmap[i], minEven)
            else:
                maxOdd = max(hashmap[i], maxOdd)
        return maxOdd - minEven