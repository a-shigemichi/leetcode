class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=1
        while i <= len(digits):
            if digits[-i] == 9:
                digits[-i] = 0
                i += 1
            else:
                digits[-i] += 1
                return digits
        digits[:0] = [1]
        return digits




def main():
    digits = [9,9,9]
    my_object = Solution()        
    judgement = my_object.plusOne(digits)
    print(judgement)

if __name__ == "__main__":
   main()