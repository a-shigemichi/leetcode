class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count ={}
        nums_nest=[]
        nums_nest.append([])
        first = 0
        index=0
        nums.sort()
        for element in nums:
            if element in count:
                first = count[element]
                count[element] = len(nums_nest)
            else:
                count[element] = len(nums_nest)
                first =0
            new_nums=[]
            for i in range(first,len(nums_nest)):
                new_nums.append(nums_nest[i]+[element])
            nums_nest+=new_nums
            index+=1
        return nums_nest
            
            





def main():
    nums = [4,4,4,1,4]
    my_object = Solution()        
    judgement = my_object.subsetsWithDup(nums)
    print(judgement)

if __name__ == "__main__":
   main()