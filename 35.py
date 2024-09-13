class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        right = len(nums)
        left = 0
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        while right > left :
            ind = (right+left) // 2
            if target == nums[ind]:
                return ind
            elif right - left == 1:
                return ind + 1
            elif target > nums[ind]:
                left = ind 
            else:
                right = ind 
            
        return ind



def main():
    nums = [1,3,5,6]
    target = 4
    my_object = Solution()        
    judgement = my_object.searchInsert(nums,target)
    print(judgement)

if __name__ == "__main__":
   main()