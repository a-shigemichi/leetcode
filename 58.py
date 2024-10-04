class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        res_count = 0
        list_s=list(s)
        for i in range(len(list_s)):
            if list_s[i].isspace():
              if count != 0:
                res_count = count
              count = 0
            else:
              count += 1
        if count != 0:
           res_count = count
        return res_count  




def main():
    s = "luffy is still joyboy"
    my_object = Solution()        
    judgement = my_object.lengthOfLastWord(s)
    print(judgement)

if __name__ == "__main__":
   main()