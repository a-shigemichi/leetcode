class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        lps = compute_lps(needle)
        
        i = j = 0
        while i < len(haystack):
            if needle[j] == haystack[i]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j  
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1 