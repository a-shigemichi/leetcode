class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        len_column=len(columnTitle)
        res=0
        for i in range(len_column):
            res+=(1+ord(columnTitle[i])-ord("A"))*26**(len_column-i-1)
        return res

def main():
    columnTitle = "AB"
    my_object = Solution()        
    judgement = my_object.titleToNumber(columnTitle)
    print(judgement)

if __name__ == "__main__":
   main()