class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start , end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = start + (end - start ) // 2
            curr_min = min(curr_min,nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1
                
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])





def main():
    nums = [3,4,5,1,2]
    my_object = Solution()        
    judgement = my_object.findMin(nums)
    print(judgement)

if __name__ == "__main__":
   main()