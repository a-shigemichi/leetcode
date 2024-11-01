class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            k = (left + right) // 2
            curr = k * (k + 1) // 2
            
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
                
        return right




def main():
    n = 5
    my_object = Solution()        
    judgement = my_object.arrangeCoins(n)
    print(judgement)

if __name__ == "__main__":
   main()