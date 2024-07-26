class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for element in nums:
            if element in dic:
                return True
            else:
                dic[element] = 1
        return False

def main():
    # nums = [1,2,3,1]
    nums = [1,2,3,4]
    my_object = Solution()        
    judgement = my_object.containsDuplicate(nums)
    print(judgement)

if __name__ == "__main__":
   main()