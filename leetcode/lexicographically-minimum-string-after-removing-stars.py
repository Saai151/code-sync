class Solution:
    def clearStars(self, s: str) -> str:
        q = []

        for index, c in enumerate(s):
            if c == "*":
                heapq.heappop(q)

            else:
                heapq.heappush(q, (c, -index))
            
        res = ['' for _ in range(len(s))]
        
        while len(q) > 0:
            c, i = heapq.heappop(q)
            i *= -1
            res[i] = c

        res_string = ""

        for char in res:
            if char != "":
                res_string += char


        return res_string