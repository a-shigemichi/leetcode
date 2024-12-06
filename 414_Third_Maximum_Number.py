class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_nums = sorted(set(nums), reverse=True)
        
        if len(distinct_nums) >= 3:
            return distinct_nums[2]
        return distinct_nums[0]
        
def main():
    nums = [3,2,1]
    my_object = Solution()        
    judgement = my_object.thirdMax(nums)
    print(judgement)

if __name__ == "__main__":
   main()