import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    


    

def main():
    piles = [3,6,7,11]
    h = 8
    my_object = Solution()        
    judgement = my_object.minEatingSpeed(piles,h)
    print(judgement)

if __name__ == "__main__":
   main()