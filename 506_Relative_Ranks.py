class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_with_index = [(s, i) for i, s in enumerate(score)]
        score_with_index.sort(key=lambda x: x[0], reverse=True)

        res = [""] * len(score)
        
        for pos, (_, idx) in enumerate(score_with_index):
            if pos == 0:
                res[idx] = "Gold Medal"
            elif pos == 1:
                res[idx] = "Silver Medal"
            elif pos == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(pos + 1)
        
        return res
            
            
            

        

def main():
    score = [1,2,3,4,5]
    my_object = Solution()
    res = my_object.findRelativeRanks(score)
    print(res)

if __name__ == "__main__":
    main()