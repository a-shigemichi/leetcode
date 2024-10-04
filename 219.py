class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_dict = {}
        
        for i, num in enumerate(nums):
            if num in num_dict and i - num_dict[num] <= k:
                return True
            num_dict[num] = i
        
        return False




def main():
    nums = [1,2,3,1,2,3]
    k = 2
    my_object = Solution()        
    judgement = my_object.containsNearbyDuplicate(nums,k)
    print(judgement)

if __name__ == "__main__":
   main()