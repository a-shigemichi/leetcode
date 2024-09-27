class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = int(a, 2)
        num_b = int(b, 2)
        
        sum_num = num_a + num_b
        return bin(sum_num)[2:]
             



def main():
    a = "11"
    b = "1"
    my_object = Solution()        
    judgement = my_object.addBinary(a,b)
    print(judgement)

if __name__ == "__main__":
   main()