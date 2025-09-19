class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Counts the number of words that can be fully typed with a malfunctioning keyboard.
        
        Args:
            text: String of words separated by single spaces
            brokenLetters: String of broken letter keys
            
        Returns:
            The number of words that can be fully typed
        """
        broken_set = set(brokenLetters)
        count = 0
        
        for word in text.split():
            if not any(char in broken_set for char in word):
                count += 1
                
        return count
