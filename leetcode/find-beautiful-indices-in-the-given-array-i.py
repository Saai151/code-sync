class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        result = set()
        
        len1 = len(a)
        len2 = len(b)

        potential_i = []
        potential_j = []


        for i in range(len(s)):
            substring_a = s[i: i + len1]
            substring_b = s[i: i + len2]
            
            if substring_a == a:
                potential_i.append(i)
            if substring_b == b:
                potential_j.append(i)
        
        print(potential_i)
        print(potential_j)

        for i in potential_i:
            for j in potential_j:
                if abs(i - j) <= k:
                    result.add(i)
                    break
        return sorted(list(result))