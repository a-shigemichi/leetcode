class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        
        for flower_pointer in range(size):
            if (flowerbed[flower_pointer] == 0 and 
                (flower_pointer == 0 or flowerbed[flower_pointer-1] == 0) and 
                (flower_pointer == size-1 or flowerbed[flower_pointer+1] == 0)):
                flowerbed[flower_pointer] = 1
                count += 1
                
        return count >= n