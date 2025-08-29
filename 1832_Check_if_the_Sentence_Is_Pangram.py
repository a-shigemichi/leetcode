class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Checks if the given sentence is a pangram (contains all 26 English letters).
        
        Time complexity: O(n) where n is the length of the sentence
        Space complexity: O(1) as we use a fixed-size set
        """
        return len(set(sentence)) == 26
