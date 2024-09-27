class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count ={}
        for element in nums:
            if element in count:
                return element
            else:
                count[element]=1
        return None




def main():
    nums = [1,3,4,2,2]
    my_object = Solution()        
    judgement = my_object.findDuplicate(nums)
    print(judgement)

if __name__ == "__main__":
   main()