class Solution(object):
    def handle_remaining_range(self,start_range_element,end_element,result_range):
        if start_range_element==end_element:
            result_range.append(f"{end_element}")
        else:
            result_range.append(f"{start_range_element}->{end_element}")
        return result_range
    
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        result_range=[]
        start_range_element=nums[0]

        for nums_index in range(1,len(nums)):
            if nums[nums_index]-nums[nums_index-1] != 1:
                if start_range_element==nums[nums_index-1]:
                    result_range.append(f"{nums[nums_index-1]}")
                else:
                  result_range.append(f"{start_range_element}->{nums[nums_index-1]}")
                start_range_element=nums[nums_index]

        result_range=self.handle_remaining_range(start_range_element,nums[-1],result_range)

        return result_range
        

def main():
    nums = [0,2,3,4,6,8,9]
    my_object = Solution()        
    result = my_object.summaryRanges(nums)
    print(result)

if __name__ == "__main__":
   main()