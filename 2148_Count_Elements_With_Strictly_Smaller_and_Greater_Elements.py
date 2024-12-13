class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
            
        nums.sort()
        min_val = nums[0]
        max_val = nums[-1]
        
        count = 0
        for num in nums:
            if min_val < num < max_val:
                count += 1
                
        return count
            
        

def main():
    nums = [11,7,2,15]
    my_object = Solution()        
    res = my_object.countElements(nums)
    print(res)

if __name__ == "__main__":
   main()