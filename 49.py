from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic_element = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for element in word:
                count[ord(element)-ord("a")] += 1
            dic_element[tuple(count)].append(word)
            
        return dic_element.values()



def main():
    anagrams = ["eat","tea","tan","ate","nat","bat"]
    my_object = Solution()
    judgement = my_object.groupAnagrams(anagrams)
    print(judgement)

if __name__ == "__main__":
    main()