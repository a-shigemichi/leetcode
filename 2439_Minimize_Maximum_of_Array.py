class Solution(object):
    def minimizeArrayValue(self, nums):
        ans = nums[0]
        prefix_sum = nums[0]

        for i in range(1, len(nums)):
            prefix_sum += nums[i]
            curr_avg = (prefix_sum + i) // (i + 1)
            ans = max(ans, curr_avg)
            
        return ans
        
def main():
    nums = [3,7,1,6]
    my_object = Solution()        
    res = my_object.minimizeArrayValue(nums)
    print(res)

if __name__ == "__main__":
   main()