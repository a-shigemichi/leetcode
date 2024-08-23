class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26
        for char in s1:
            count_s1[ord(char) - ord('a')] += 1

        for i in range(len(s1)):
            count_s2[ord(s2[i]) - ord('a')] += 1

        if count_s1 == count_s2:
            return True

        for r in range(len(s1), len(s2)):
            count_s2[ord(s2[r]) - ord('a')] += 1
            count_s2[ord(s2[r - len(s1)]) - ord('a')] -= 1

            if count_s1 == count_s2:
                return True

        return False

            




def main():
    s = "ab"
    s2 = "eidbaooo"
    my_object = Solution()        
    judgement = my_object.checkInclusion(s,s2)
    print(judgement)

if __name__ == "__main__":
   main()