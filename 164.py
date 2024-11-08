class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        res=0
        nums.sort()
        if len(nums)<=2:
            return 0
        else:
            while i<len(nums)-1:
                num=nums[i+1]-nums[i]
                res=max(res,num)
                i+=1
            return res


def main():
    nums = [3,6,9,1]
    my_object = Solution()        
    judgement = my_object.maximumGap(nums)
    print(judgement)

if __name__ == "__main__":
   main()