class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result = []
        
        for interval in intervals:
            end = interval[1]
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if starts[mid][0] >= end:
                    right = mid
                else:
                    left = mid + 1
            
            result.append(starts[left][1] if left < n else -1)
        
        return result