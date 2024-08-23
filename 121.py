class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = prices[0]
        end = None
        res = 0
        res2 = 0
        for element in prices[1:]:
            if element < start:
                if end != None :
                    res2 = end -start
                    if res < res2:
                        res = res2
                start = element
                end = None
            elif end == None:
                end = element
            elif element > end:
                end = element
        if end != None :
                    res2 = end -start
                    if res < res2:
                        res = res2
        return res

             
        



def main():
    prices = [7,1,5,3,6,4]
    my_object = Solution()        
    judgement = my_object.maxProfit(prices)
    print(judgement)

if __name__ == "__main__":
   main()