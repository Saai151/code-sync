class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {}

        hashmap['('] = ')'
        hashmap['{'] = '}'
        hashmap['['] = ']'

        stack = []

        for char in s:
            if char in hashmap:
                stack.append(char)
            elif len(stack) > 0 and hashmap[stack[-1]] == char:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        return False