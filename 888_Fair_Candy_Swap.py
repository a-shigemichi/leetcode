class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        aliceTotal = sum(aliceSizes)
        bobTotal = sum(bobSizes)
        diff = (aliceTotal - bobTotal) // 2
        bobSet = set(bobSizes)
        
        for aliceCandy in aliceSizes:
            target = aliceCandy - diff
            if target in bobSet:
                return [aliceCandy,target]
        

def main():
    aliceSizes = [1,1]
    bobSizes = [2,2]
    my_object = Solution()        
    judgement = my_object.fairCandySwap(aliceSizes,bobSizes)
    print(judgement)

if __name__ == "__main__":
   main()