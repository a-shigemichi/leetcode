class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = list(s)
        new_word = []
        for element in word:
            if element.isalnum():
                lower_ele = element.lower()
                new_word.append(lower_ele)
        new_len = len(new_word)
        for index in range(new_len):
            if new_word[index] != new_word[new_len-index-1]:
                return False
        return True


        



def main():
    s = "A man, a plan, a canal: Panama"
    my_object = Solution()        
    judgement = my_object.isPalindrome(s)
    print(judgement)

if __name__ == "__main__":
   main()