class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        pos = intervals[0][1]
        ans = 0
        for i in range(1,  len(intervals)):
            if intervals[i][0] < pos:
                ans += 1
            else:
                pos = intervals[i][1]
        return ans
