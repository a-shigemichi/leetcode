class Solution(object):
    def triangleNumber(self, nums):
      if len(nums) < 3:
          return 0
      
      nums.sort()
      count = 0
      n = len(nums)
      
      for i in range(n-1, 1, -1):
          left = 0
          right = i - 1
          
          while left < right:
              if nums[left] + nums[right] > nums[i]:
                  count += right - left
                  right -= 1
              else:
                  left += 1
                  
      return count

def main():
    nums = [2,2,3,4]
    my_object = Solution()        
    judgement = my_object.triangleNumber(nums)
    print(judgement)

if __name__ == "__main__":
   main()