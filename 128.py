class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
            
                            




def main():
    nums = [10,4,20,1,3,2]
    my_object = Solution()        
    judgement = my_object.longestConsecutive(nums)
    print(judgement)

if __name__ == "__main__":
   main()