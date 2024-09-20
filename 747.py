class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        stack=[]
        stack.append(0)
        stack.append(0)
        for i in range(len(nums)):
          if nums[i] > stack[-1]:
            stack.pop()
            if nums[i] > stack[0]:
              stack.insert(0, nums[i])
              ind = i
            else:
              stack.append(nums[i])
        if stack[0]>=2*stack[1]:
           return ind
        else:
           return -1
                




def main():
    nums = [3,6,1,0]
    my_object = Solution()        
    judgement = my_object.dominantIndex(nums)
    print(judgement)

if __name__ == "__main__":
   main()