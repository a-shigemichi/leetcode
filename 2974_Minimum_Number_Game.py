from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        """
        Simulates a game between Alice and Bob where they alternately remove minimum elements
        from nums and append them to result array in a specific order.
        
        Alice removes minimum first, then Bob removes minimum.
        Bob appends his element to result first, then Alice appends hers.
        """
        nums.sort()
        arr = []
        
        for i in range(0, len(nums), 2):
            alice_element = nums[i]
            bob_element = nums[i + 1]
            
            arr.append(bob_element)
            arr.append(alice_element)
        
        return arr
