class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []
        for i in range(n):
            stack.append("(")
        for i in range(n):
            stack.append(")")
        result.append("".join(stack))
        
        k = n
        for i in range(n):
            k += i
            stack[k-1],stack[k] = stack[k],stack[k-1]
            result.append("".join(stack))
            
        
        return result
    
def main():
    nums = 3
    my_object = Solution()        
    judgement = my_object.generateParenthesis(nums)
    print(judgement)

if __name__ == "__main__":
   main()