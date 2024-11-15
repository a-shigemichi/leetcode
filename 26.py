class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        k = 1  
        
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        
        return k
                    


def main():
    nums = [1,1,2]
    my_object = Solution()
    judgement = my_object.removeElement(nums,my_object)
    print(judgement)

if __name__ == "__main__":
    main()