class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s = {} 
        dic_t = {}
        s_list = list(s)
        t_list = list(t)
        for element in s_list:
            if element in dic_s:
                dic_s[element] += 1
            else:
                dic_s[element] = 1

        for element in t_list:
            if element in dic_t:
                dic_t[element] += 1
            else:
                dic_t[element] = 1
        
        if dic_s == dic_t:
            return True
        else:
            return False

def main():
    # s = "anagram"
    # t = "nagaram"
    s = "rat"
    t = "car"
    my_object = Solution()
    judgement = my_object.isAnagram(s,t)
    print(judgement)

if __name__ == "__main__":
    main()