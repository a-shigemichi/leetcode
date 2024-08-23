class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        for element in s:
            if element in stack:
                ind = stack.index(element)
                length = len(stack)
                if res < length:
                    res = length
                for i in range(ind+1):
                    stack.pop(0)
            stack.append(element)
            print(stack)
        
        length = len(stack)
        if res < length:
            res = length
        return res
        


def main():
    s = "pwwkew"
    my_object = Solution()        
    judgement = my_object.lengthOfLongestSubstring(s)
    print(judgement)

if __name__ == "__main__":
   main()