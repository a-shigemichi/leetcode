class Solution:
    def sortSentence(self, s: str) -> str:
        """
        Reconstruct the original sentence from a shuffled sentence.
        
        Each word in the shuffled sentence has a 1-indexed position number 
        appended to it. We need to sort the words by their original positions
        and remove the position numbers.
        
        Args:
            s: Shuffled sentence where each word ends with its 1-indexed position
            
        Returns:
            str: Original sentence with words in correct order
        """
        words = s.split()
        result = [''] * len(words)
        
        for word in words:
            position = int(word[-1])
            actual_word = word[:-1]
            result[position - 1] = actual_word
        
        return ' '.join(result)
