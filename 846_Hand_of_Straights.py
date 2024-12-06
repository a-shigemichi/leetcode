from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        unique_cards = sorted(count.keys())
        
        while unique_cards:
            start = unique_cards[0]
            
            for i in range(groupSize):
                curr_card = start + i
                
                if curr_card not in count:
                    return False
                    
                count[curr_card] -= 1
                
                if count[curr_card] == 0:
                    if curr_card != unique_cards[0]:
                        return False
                    unique_cards.pop(0)
        
        return True


def main():
    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 3
    my_object = Solution()        
    judgement = my_object.isNStraightHand(hand,groupSize)
    print(judgement)

if __name__ == "__main__":
   main()