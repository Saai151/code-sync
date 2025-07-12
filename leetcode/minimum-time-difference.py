class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            hour = int(time[0:2])
            minute = int(time[3:5])
            return hour * 60 + minute
        
        minutes = []

        for time in timePoints:
            minutes.append(convert(time))

        minutes.sort()

        minDifference = float('inf')


        for i in range(len(minutes) - 1):   
            difference = minutes[i + 1] - minutes[i]
            minDifference = min(difference, minDifference)

        return min(minDifference, 24*60 - minutes[-1] + minutes[0])