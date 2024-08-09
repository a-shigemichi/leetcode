class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        dic = []
        word_num = 0
        element_num = 0
        for word in strs:
            word_num += 1
            for element in word:
                element_num += 1
                if word_num == 1:
                    dic.append(element)
                elif element_num <= len(dic) and dic[element_num-1] != element:
                    del dic[element_num-1:]
                    break
            if element_num < len(dic):
                del dic[element_num:]
            element_num = 0
            del dic[element_num-1:]
        dic = "".join(dic)
        return dic
