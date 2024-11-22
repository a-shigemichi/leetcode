class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res=[]
        s=sorted(s)
        t=sorted(list(t))
        for element in t:
            if element not in s:
                res.append(element)
            else:
                s.pop(0)
        return ''.join(res)
              

def main():
    s = "a"
    t = "aa"
    my_object = Solution()        
    judgement = my_object.findTheDifference(s,t)
    print(judgement)

if __name__ == "__main__":
   main()