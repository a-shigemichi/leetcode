class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        res=[]
        for element in nums:
            if element not in dic:
                dic[element] = 1
        for i in range(1,len(nums)+1):
            if i not in dic:
                res.append(i)
        return res



def main():
    nums = [4,3,2,7,8,2,3,1]
    my_object = Solution()        
    judgement = my_object.findDisappearedNumbers(nums)
    print(judgement)

if __name__ == "__main__":
   main()