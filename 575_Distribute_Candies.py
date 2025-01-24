class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_num = len(candyType)
        candy_type_hash={}
        candy_type_num=0
        if candy_num==0:
            return 0
        
        for candy in candyType:
            if candy not in candy_type_hash:
                candy_type_hash[candy]=1
                candy_type_num+=1
        if candy_num/2 <= candy_type_num:
            return candy_num//2
        else:
          return  candy_type_num
        