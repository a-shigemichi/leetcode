class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []
        
        for num in nums:
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
                
        return len(tails) 




def main():
    nums = [10,9,2,5,3,7,101,18]
    my_object = Solution()        
    judgement = my_object.lengthOfLIS(nums)
    print(judgement)

if __name__ == "__main__":
   main()