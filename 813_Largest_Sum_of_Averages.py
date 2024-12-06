class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        def solve(start, parts):
            if parts == 0 and start == n:
                return 0
            if parts == 0 or start == n:
                return float('-inf')
            
            if dp[start][parts] != -1:
                return dp[start][parts]
            
            max_score = float('-inf')
            for end in range(start, n):
                avg = (prefix[end + 1] - prefix[start]) / (end - start + 1)
                next_score = solve(end + 1, parts - 1)
                if next_score != float('-inf'):
                    max_score = max(max_score, avg + next_score)
            
            dp[start][parts] = max_score
            return max_score
        
        return solve(0, k)   

def main():
    nums = [1,2,3,4,5,6,7]
    k = 4
    my_object = Solution()        
    judgement = my_object.largestSumOfAverages(nums,k)
    print(judgement)

if __name__ == "__main__":
   main()