class Solution(object):
    def findLUSlength(self, strs):
        def isSubsequence(s, t):
            t_idx = 0
            for char in s:
                while t_idx < len(t) and t[t_idx] != char:
                    t_idx += 1
                if t_idx >= len(t):
                    return False
                t_idx += 1
            return True
        
        n = len(strs)
        max_len = -1
        
        for i in range(n):
            is_uncommon = True
            for j in range(n):
                if i != j and isSubsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break
            
            if is_uncommon:
                max_len = max(max_len, len(strs[i]))
        
        return max_len
        
def main():
    strs = ["aba","cdc","eae"]
    my_object = Solution()
    judgement = my_object.findLUSlength(strs)
    print(judgement)

if __name__ == "__main__":
    main()