class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack =[]
        res = [0]*len(temperatures)

        for index,element in enumerate(temperatures):
            while stack and element > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = index-stackInd
            stack.append((element,index))
        return res


def main():
    nums = [73,74,75,71,69,72,76,73]
    my_object = Solution()        
    judgement = my_object.dailyTemperatures(nums)
    print(judgement)

if __name__ == "__main__":
   main()