class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_nest=[]
        nums_nest.append([])
        for element in nums:
            new_nums=[]
            for subset in nums_nest:
                new_nums.append(subset+[element])
            nums_nest+=new_nums
        return nums_nest




def main():
    nums = [1,2,3]
    my_object = Solution()        
    judgement = my_object.subsets(nums)
    print(judgement)

if __name__ == "__main__":
   main()