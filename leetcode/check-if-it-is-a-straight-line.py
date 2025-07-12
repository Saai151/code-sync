class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        n = len(coordinates)
        if (coordinates[n - 1][0] - coordinates[0][0]) == 0:
            for x, y in coordinates:
                if x == coordinates[0][0]:
                    continue
                else:
                    return False
            return True
            
        m = (coordinates[n - 1][1] - coordinates[0][1]) / (coordinates[n - 1][0] - coordinates[0][0])

        x1 = coordinates[0][0]
        y1 = coordinates[0][1]

        for x,y in coordinates[1:]:
            if x1 - x != 0 and (y1 - y)/(x1 - x) == m:
                continue
            else:
                return False
        return True