class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        jumps = curr_max = next_max = 0
        
        for i in range(len(nums) - 1):
            next_max = max(next_max, i + nums[i])
            
            if i == curr_max:
                jumps += 1
                curr_max = next_max
                
                if curr_max >= len(nums) - 1:
                    break
                    
        return jumps
    