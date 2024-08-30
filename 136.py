class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for element in nums:
            if element in dic:   
                dic[element] += 1
            else: 
                dic[element] = 1
        for key, value in dic.items():
            if value == 1:
                return key



def main():
    pnums = [4,1,2,1,2]
    my_object = Solution()        
    judgement = my_object.singleNumber(pnums)
    print(judgement)

if __name__ == "__main__":
   main()