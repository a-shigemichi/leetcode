class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        for element in nums:
          if element / 2 == element // 2:
             stack.insert(0,element)
          else:
             stack.append(element)
        return stack



def main():
    nums = [1,0]
    my_object = Solution()        
    judgement = my_object.sortArrayByParity(nums)
    print(judgement)

if __name__ == "__main__":
   main()