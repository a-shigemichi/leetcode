class Solution(object):
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones
        

def main():
    nums = [2,2,3,2]
    my_object = Solution()        
    judgement = my_object.singleNumber(nums)
    print(judgement)

if __name__ == "__main__":
   main()