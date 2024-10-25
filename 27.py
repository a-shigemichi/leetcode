class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
                


def main():
    nums = [3,2,2,3] 
    val = 3
    my_object = Solution()
    judgement = my_object.removeElement(nums,val)
    print(judgement)

if __name__ == "__main__":
    main()