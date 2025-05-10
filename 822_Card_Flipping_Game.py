from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """
        Find the minimum good integer after flipping cards.
        
        A card has a positive integer on the front (fronts[i]) and another on the back (backs[i]).
        Initially, all cards are placed with the front number facing up.
        You may flip over any number of cards (possibly zero).
        
        After flipping, an integer is considered "good" if it is facing down on some card
        and not facing up on any card.
        
        Args:
            fronts (List[int]): A list of positive integers on the front of each card.
            backs (List[int]): A list of positive integers on the back of each card.
            
        Returns:
            int: The minimum possible good integer after flipping cards.
                 Return 0 if there are no good integers.
        """
        same = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same.add(fronts[i])

        min_good = None

        for i in range(len(fronts)):
            if fronts[i] not in same:
                if min_good is None or fronts[i] < min_good:
                    min_good = fronts[i]

            if backs[i] not in same:
                if min_good is None or backs[i] < min_good:
                    min_good = backs[i]

        return 0 if min_good is None else min_good
    