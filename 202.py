class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        def extract_digits_math(n):
            digits = []
            number = abs(n)
            
            while number > 0:
                digits.append(number % 10)
                number //= 10
            digits = digits[::-1]
            return digits
        def sum_of_squares(digits):
            sum = 0
            for i in range(len(digits)):
                sum += digits[i]**2
            return sum
            
        while n != 1:
            digits = extract_digits_math(n)
            n = sum_of_squares(digits)
            if n in dic:
                return False
            else:
                dic[n] = 1
        return True

def main():
    n = 2
    my_object = Solution()        
    judgement = my_object.isHappy(n)
    print(judgement)

if __name__ == "__main__":
   main()