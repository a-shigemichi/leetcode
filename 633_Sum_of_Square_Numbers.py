class Solution(object):
    def judgeSquareSum(self, c):
        if c < 0:
            return False
            
        a = 0
        while a * a <= c:
            b = int((c - a * a) ** 0.5)
            if a * a + b * b == c:
                return True
            a += 1
        return False
        
def main():
    c = 5
    my_object = Solution()        
    judgement = my_object.judgeSquareSum(c)
    print(judgement)

if __name__ == "__main__":
   main()