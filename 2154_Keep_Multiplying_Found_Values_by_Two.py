class Solution(object):
    def findFinalValue(self, nums, original):
        current = original
        while current in nums:
            current *= 2
        
        return current
        


def main():
    nums = [5,3,6,1,12]
    original = 3
    my_object = Solution()        
    res = my_object.findFinalValue(nums,original)
    print(res)

if __name__ == "__main__":
   main()