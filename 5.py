class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res_l = 0
        res_r = 0
        res = 0
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if res <= right-left+1:
                    res = right-left+1
                    res_l = left
                    res_r = right
                left -= 1
                right += 1
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if res <= right-left+1:
                    res = right-left+1
                    res_l = left
                    res_r = right
                left -= 1
                right += 1
                
        return s[res_l:res_r+1]
         
        


def main():
    s="aacabdkacaa"
    my_object = Solution()        
    judgement = my_object.longestPalindrome(s)
    print(judgement)

if __name__ == "__main__":
   main()