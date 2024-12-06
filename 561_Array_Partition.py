class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        max_sum=0
        while i < len(nums):
            max_sum+=nums[i]
            i+=2
        return max_sum



def main():
    nums = [1,4,3,2]
    my_object = Solution()        
    judgement = my_object.arrayPairSum(nums)
    print(judgement)

if __name__ == "__main__":
   main()