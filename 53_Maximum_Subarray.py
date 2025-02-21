class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    my_object = Solution()
    judgement = my_object.maxSubArray(nums)
    print(judgement)

if __name__ == "__main__":
    main()