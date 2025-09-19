class Solution:
    def partitionString(self, s: str) -> int:
        """
        Partitions the string into minimum number of substrings where each substring has unique characters.
        
        Args:
            s: The input string to partition
            
        Returns:
            The minimum number of substrings needed for the partition
        """
        seen = set()
        partitions = 1
        
        for char in s:
            if char in seen:
                partitions += 1
                seen.clear()
            seen.add(char)
            
        return partitions
