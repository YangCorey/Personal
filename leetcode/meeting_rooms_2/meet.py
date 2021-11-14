from typing import List

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [1,5] [1,20], [2,4], [4,6] [6,8]
        intervals.sort(key = lambda x: x[0])
        rooms = 1#
        temp_rooms = 0#
        interval_hist =  []
        for ind, inter in enumerate(intervals): #6,8
            temp_rooms += 1
            start,end = inter
            while interval_hist != [] and interval_hist[0] <= start:
                temp_rooms -= 1
                heappop(interval_hist)
            if temp_rooms > rooms:
                rooms = temp_rooms #3
            heappush(interval_hist,end)#20
            


        return rooms

