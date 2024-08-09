class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack =[]
        for element in tokens:
            if element == "+":
                stack.append(stack.pop() + stack.pop())
            elif element == "-":
                a = stack.pop()
                b = stack.pop() 
                stack.append(b-a)
            elif element == "*":
                stack.append(stack.pop() * stack.pop())
            elif element == "/":
                a = stack.pop()
                b = stack.pop() 
                stack.append(int(float(b)/a))
            else:
                stack.append(int(element))
        return stack[0]

        


def main():
    # nums = [1,2,3,1]
    nums = ["2","1","+","3","*"]
    my_object = Solution()        
    judgement = my_object.evalRPN(nums)
    print(judgement)

if __name__ == "__main__":
   main()