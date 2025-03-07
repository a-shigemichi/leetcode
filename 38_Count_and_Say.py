class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Returns the nth term of the countAndSay sequence.
        
        The countAndSay sequence is defined as:
        1. The first term is "1"
        2. Each subsequent term is derived by describing the previous term:
          count the number of consecutive identical digits, then append the count 
          followed by the digit.
        
        :param n: A positive integer representing the sequence position
        :return: The nth element of the countAndSay sequence as a string
        """
        if n == 1:
            return "1"

        prev_string = self.countAndSay(n - 1)
        
        result = ""
        count = 1
        
        for i in range(len(prev_string)):
            if i + 1 < len(prev_string) and prev_string[i] == prev_string[i + 1]:
                count += 1
            else:
                result += str(count) + prev_string[i]
                count = 1
        
        return result     