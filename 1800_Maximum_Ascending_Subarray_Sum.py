class Solution(object):
    def isAscendingOrder(self, nums, sub_array_end_index):
        if nums[sub_array_end_index] > nums[sub_array_end_index-1]:
          return True
        else:
          return False
        
    def maxAscendingSum(self, nums):
        sub_array_start_index=0
        sub_array_end_index=0
        subarray_sum=nums[sub_array_start_index]
        max_subarray_sum=0
        while sub_array_end_index<len(nums)-1:
            sub_array_end_index+=1
            if(self.isAscendingOrder(nums, sub_array_end_index)):
               subarray_sum+=nums[sub_array_end_index]
            else:
               max_subarray_sum=max(max_subarray_sum,subarray_sum)
               sub_array_start_index=sub_array_end_index
               subarray_sum=nums[sub_array_start_index]
        max_subarray_sum=max(max_subarray_sum,subarray_sum)
        return max_subarray_sum
       
def main():
    nums = [10,20,30,5,10,50]
    my_object = Solution()        
    res = my_object.maxAscendingSum(nums)
    print(res)

if __name__ == "__main__":
   main()