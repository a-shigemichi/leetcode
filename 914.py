from math import gcd
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        nums=[]
        count={}
        for element in deck:
            if element in count:
                count[element]+=1
            else:
                count[element]=1
                nums.append(element)
        min_num = nums[0]
        if len(nums) > 1:
            gcd_res = gcd(count[nums[0]],count[nums[1]])
        elif count[nums[0]] > 1:
            return True
        else:
            return False
        for i in range(len(nums)):
            gcd_res = gcd(gcd_res,count[nums[i]])
        
        if gcd_res == 1:
            return False
        else:
            return True





def main():
    deck = [1,1,1,2,2,2,3,3,3,3,3,3]
    my_object = Solution()        
    judgement = my_object.hasGroupsSizeX(deck)
    print(judgement)

if __name__ == "__main__":
   main()