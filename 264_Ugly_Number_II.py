class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1] * n
    
        i2 = i3 = i5 = 0
        
        next2 = 2
        next3 = 3
        next5 = 5
        
        for i in range(1, n):
            ugly[i] = min(next2, next3, next5)
            
            if ugly[i] == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if ugly[i] == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if ugly[i] == next5:
                i5 += 1
                next5 = ugly[i5] * 5
        
        return ugly[n-1]




def main():
    n = 10
    my_object = Solution()        
    judgement = my_object.nthUglyNumber(n)
    print(judgement)

if __name__ == "__main__":
   main()