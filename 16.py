class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == target:
                    return curr_sum
                
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
        


def main():
    nums = [-1,2,1,-4]
    target = 1
    my_object = Solution()        
    judgement = my_object.threeSumClosest(nums,target)
    print(judgement)

if __name__ == "__main__":
   main()