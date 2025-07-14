class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start times

        intervals.sort(key=lambda x: x[0])
        
        for i in range(len(intervals) - 1):
            start = intervals[i + 1][0]
            end = intervals[i][1]

            if end >= start:
                intervals[i + 1][0] = intervals[i][0]
                intervals[i + 1][1] = max(intervals[i + 1][1], intervals[i][1])


        d = {}
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            d[start] = end
        
        res = []
        for key, val in d.items():
            res.append([key,val])
        return res