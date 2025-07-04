from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        Sort people's names by their heights in descending order.
        
        Args:
            names: List of people's names
            heights: List of corresponding heights (distinct positive integers)
            
        Returns:
            List[str]: Names sorted by heights in descending order
        """
        paired = zip(names, heights)
        sorted_pairs = sorted(paired, key=lambda x: x[1], reverse=True)
        return [name for name, height in sorted_pairs]
