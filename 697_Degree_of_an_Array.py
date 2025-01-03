class Solution(object):
    def findShortestSubArray(self, nums):
        count = {}
        first_index = {}
        last_index = {}
        
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            last_index[num] = i
            
            if num not in first_index:
                first_index[num] = i
        
        degree = max(count.values())
        
        min_length = len(nums)
        for num in count:
            if count[num] == degree:
                length = last_index[num] - first_index[num] + 1
                min_length = min(min_length, length)
        
        return min_length

def main():
    nums = [1,2,2,3,1,4,2]
    my_object = Solution()        
    judgement = my_object.findShortestSubArray(nums)
    print(judgement)

if __name__ == "__main__":
   main()