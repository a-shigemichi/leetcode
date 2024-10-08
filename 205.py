class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for c1, c2 in zip(s, t):
            if c1 not in s_to_t and c2 not in t_to_s:
                s_to_t[c1] = c2
                t_to_s[c2] = c1
            elif s_to_t.get(c1) != c2 or t_to_s.get(c2) != c1:
                return False
        
        return True
        


def main():
    s = "egg"
    t = "add"
    my_object = Solution()        
    judgement = my_object.isIsomorphic(s,t)
    print(judgement)

if __name__ == "__main__":
   main()