class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        res=[0]*len(queries)
        words_f=[]
        for i in range (len(words)):
          smallest_alp=25
          count = [0] * 26
          for element in words[i]:
            smallest_alp=min(smallest_alp,ord(element)-ord("a"))
            count[ord(element)-ord("a")] += 1
          words_f.append(count[smallest_alp])
        for i in range (len(queries)):
          smallest_alp=25
          count = [0] * 26
          for element in queries[i]:
            smallest_alp=min(smallest_alp,ord(element)-ord("a"))
            count[ord(element)-ord("a")] += 1
          for j in range(len(words)):
            if count[smallest_alp]<words_f[j]:
               res[i] += 1
        return res
             
            



def main():
    queries = ["bbb","cc"]
    words = ["a","aa","aaa","aaaa"]
    my_object = Solution()        
    judgement = my_object.numSmallerByFrequency(queries,words)
    print(judgement)

if __name__ == "__main__":
   main()