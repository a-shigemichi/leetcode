class Solution(object):
    def majorityElement(self, nums):
        count = {}
        n = len(nums)
        result = []
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        majority_freq = n // 3
        for num, freq in count.items():
            if freq > majority_freq:
                result.append(num)
                
        return result
    
def main():
    nums = [1,2,3,4]
    my_object = Solution()        
    judgement = my_object.productExceptSelf(nums)
    print(judgement)

if __name__ == "__main__":
   main()
