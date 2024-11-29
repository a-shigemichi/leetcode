class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        curr_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0

def main():
    target = 7
    nums = [2,3,1,2,4,3]
    my_object = Solution()        
    judgement = my_object.minSubArrayLen(target,nums)
    print(judgement)

if __name__ == "__main__":
   main()