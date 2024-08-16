class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i, element in enumerate(nums):
            if element > 0:
                break

            if i > 0 and element == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                Sum = element + nums[l] + nums[r]
                if Sum > 0:
                    r -= 1
                elif Sum < 0:
                    l += 1
                else:
                    res.append([element, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res





def main():
    nums = [-1,0,1,2,-1,-4]
    my_object = Solution()        
    judgement = my_object.threeSum(nums)
    print(judgement)

if __name__ == "__main__":
   main()