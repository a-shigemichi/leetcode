class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, current):
          if target == 0:
              result.append(current[:])
              return
          
          for i in range(start, len(candidates)):
              if candidates[i] > target:
                  break
                  
              current.append(candidates[i])
              backtrack(i, target - candidates[i], current)
              current.pop()
    
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result
            



            


def main():
    candidates = [3,5,7]
    target = 10
    my_object = Solution()        
    judgement = my_object.combinationSum(candidates,target)
    print(judgement)

if __name__ == "__main__":
   main()