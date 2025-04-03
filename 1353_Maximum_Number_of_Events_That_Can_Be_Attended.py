import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Calculate the maximum number of events that can be attended.
        
        For each day, we greedily attend the event that ends the earliest among
        all available events on that day.
        
        Args:
            events (List[List[int]]): A list of events where events[i] = [startDay_i, endDay_i].
                                     Each event i starts at startDay_i and ends at endDay_i.
        
        Returns:
            int: The maximum number of events that can be attended.
        """
        events.sort()
        
        event_count = 0
        event_index = 0
        n = len(events)
        available_events = [] 
        
        max_day = max(event[1] for event in events)

        for day in range(1, max_day + 1):
            while event_index < n and events[event_index][0] <= day:
                heapq.heappush(available_events, events[event_index][1])
                event_index += 1
            
            while available_events and available_events[0] < day:
                heapq.heappop(available_events)

            if available_events:
                heapq.heappop(available_events)
                event_count += 1
        
        return event_count
    