class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while (stack and temperatures[stack[-1]] < temperatures[i]):
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans