class Solution(object):
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[len(s)]

def main():
    s = "leetcode"
    wordDict = ["leet","code"]
    my_object = Solution()        
    judgement = my_object.wordBreak(s,wordDict)
    print(judgement)

if __name__ == "__main__":
   main()