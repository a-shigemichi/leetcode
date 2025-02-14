class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Find the smallest character in letters that is lexicographically greater than target.
        If no such character exists, return the first character in letters.
        
        Args:
            letters (List[str]): Sorted array of characters in non-decreasing order
            target (str): Target character to find the next greatest letter
            
        Returns:
            str: Smallest character greater than target, or first character if none exists
            
        """
        left = 0
        right = len(letters) - 1
        
        if target >= letters[-1]:
            return letters[0]
        
        while left < right:
            mid = left + (right - left) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
                
        return letters[left]