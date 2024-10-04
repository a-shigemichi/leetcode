class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return res
    


def main():
    height = [1,8,6,2,5,4,8,3,7]
    my_object = Solution()        
    judgement = my_object.maxArea(height)
    print(judgement)

if __name__ == "__main__":
   main()