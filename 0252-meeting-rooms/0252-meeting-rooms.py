class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals = list(sorted(intervals, key = lambda x: x[1]))
        # print(intervals)
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True