class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output_nums = []
        for i in range(len(nums)):
            val = target - nums[i]
            for j in range(i+1, len(nums)):
                if val == nums[j]:
                    output_nums.append(i)
                    output_nums.append(j)
                    return output_nums
        

def main():
    # nums = [2,7,11,15]
    # target = 9
    nums = [3,2,4]
    target = 6
    my_object = Solution()
    judgement = my_object.twoSum(nums,target)
    print(judgement)

if __name__ == "__main__":
    main()