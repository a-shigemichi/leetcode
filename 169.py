class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}

        if len(nums) == 1:
            return nums[0]
            
        for element in nums:
            if element in count:
                count[element] += 1
                if count[element]>len(nums)/2:
                    return element
            else:
                count[element] = 1




def main():
    nums = [2,2,1,1,1,2,2]
    my_object = Solution()        
    judgement = my_object.majorityElement(nums)
    print(judgement)

if __name__ == "__main__":
   main()