class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        spec = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= spec
            spec *= nums[i]
        return res


def main():
    # nums = [1,2,3,1]
    nums = [1,2,3,4]
    my_object = Solution()        
    judgement = my_object.productExceptSelf(nums)
    print(judgement)

if __name__ == "__main__":
   main()