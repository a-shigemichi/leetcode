from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        Given an integer array deck, return an ordering of the deck that would 
        reveal the cards in increasing order.
        
        The revealing process:
        1. Take the top card, reveal it, and remove it from the deck.
        2. If there are still cards, put the next top card at the bottom.
        3. Repeat until all cards are revealed.
        
        Args:
            deck (List[int]): Array of integers representing cards
            
        Returns:
            List[int]: An ordering of the deck that reveals cards in increasing order
        """
        deck.sort()
        result = deque()
        
        for card in reversed(deck):
            if result:
                result.appendleft(result.pop())
            result.appendleft(card)
        
        return list(result)
    