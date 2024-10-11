class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1




def main():
    nums = [0,1,0,3,12]
    my_object = Solution()        
    judgement = my_object.moveZeroes(nums)
    print(judgement)

if __name__ == "__main__":
   main()