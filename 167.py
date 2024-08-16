class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]


def main():
    target= 8
    numbers = [2,4,4,11,15]
    my_object = Solution()        
    judgement = my_object.twoSum(numbers,target)
    print(judgement)

if __name__ == "__main__":
   main()