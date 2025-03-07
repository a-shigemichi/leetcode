class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Sorts the characters of string s according to the custom order defined in string order.
        
        Args:
            order: A string where all characters are unique and define the custom sorting order
            s: The string to be permuted
            
        Returns:
            A permutation of s that satisfies the ordering property defined by order
        """
        char_to_index = {char: i for i, char in enumerate(order)}

        max_index = len(order)

        result = sorted(s, key=lambda char: char_to_index.get(char, max_index + ord(char)))

        return ''.join(result)
    