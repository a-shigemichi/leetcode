class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        """
        Find the index of peak element in a mountain array.
        A mountain array increases strictly until it reaches a peak element, then decreases strictly afterward.
        
        Args:
            arr (List[int]): A mountain array where values first increase then decrease
            
        Returns:
            int: The index of the peak element
            
        Time Complexity:
            O(log n) where n is the length of the array
            
        Space Complexity:
            O(1)
            
        """
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
                
        return left
    