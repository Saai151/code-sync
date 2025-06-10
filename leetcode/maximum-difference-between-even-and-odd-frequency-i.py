# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
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
```