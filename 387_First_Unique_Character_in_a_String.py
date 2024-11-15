class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        first_index = {}
        
        for i, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1
            if char not in first_index:
                first_index[char] = i
        
        result = float('inf')
        for char, count in char_count.items():
            if count == 1:
                result = min(result, first_index[char])
        
        return result if result != float('inf') else -1
                



def main():
    s = "loveleetcode"
    my_object = Solution()        
    judgement = my_object.firstUniqChar(s)
    print(judgement)

if __name__ == "__main__":
   main()