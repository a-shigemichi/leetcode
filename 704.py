class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #O(logn)

        left = 0
        right = len(nums)-1
        
        while left <= right:
            ind = (left + right) // 2
            if target == nums[ind]:
                return ind
            elif target > nums[ind]:
                left = ind + 1
            else:
                right = ind - 1
        
        return -1






def main():
    nums = [-1,0,3,5,9,12]
    target = 9
    my_object = Solution()        
    judgement = my_object.search(nums,target)
    print(judgement)

if __name__ == "__main__":
   main()