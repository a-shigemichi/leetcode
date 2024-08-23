from collections import deque
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        k_count = 0
        res = 0
        queue = deque()
        s_l=0
        dic = {}
        for element in s:
            if element in dic:
                continue
            else:
                dic[element] = 1
                for r in range(len(s)):
                    if s[r] != element:
                        k_count += 1
                        if k_count > k:
                            res = max(res, len(queue))
                            while queue and queue[0] == element:
                                queue.popleft()
                            if queue:
                                queue.popleft()
                            else:
                                continue    
                            k_count -= 1
                    queue.append(s[r])
                
                res = max(res,len(queue))
                queue.clear()
                k_count=0
        return res

            





def main():
    s = "ABAA"
    k = 0
    my_object = Solution()        
    judgement = my_object.characterReplacement(s,k)
    print(judgement)

if __name__ == "__main__":
   main()