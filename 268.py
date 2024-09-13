class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=len(nums)*(len(nums)+1)/2
        for element in nums:
            sum = sum-element
        return int(sum)




def main():
    nums = [9,6,4,2,3,5,7,0,1]
    my_object = Solution()        
    judgement = my_object.missingNumber(nums)
    print(judgement)

if __name__ == "__main__":
   main()