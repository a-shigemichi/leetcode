from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Find all start indices of anagrams of string p in string s.
        
        An anagram is a word or phrase formed by rearranging the letters of a different
        word or phrase, typically using all the original letters exactly once.
        
        Args:
            s (str): The source string to search within.
            p (str): The target string whose anagrams are to be found in s.
            
        Returns:
            List[int]: A list of all the starting indices of p's anagrams in s.
        """
        if len(p) > len(s):
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26

        for char in p:
            p_count[ord(char) - ord('a')] += 1
        
        result = []

        for i in range(len(p)):
            s_count[ord(s[i]) - ord('a')] += 1

        if p_count == s_count:
            result.append(0)

        for i in range(len(p), len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

            s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            if p_count == s_count:
                result.append(i - len(p) + 1)
        
        return result
    