class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(counter, curr_perm, length):
            if len(curr_perm) == length:
                results.append(curr_perm[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    curr_perm.append(num)
                    backtrack(counter, curr_perm, length)
                    curr_perm.pop()
                    counter[num] += 1
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        results = []
        backtrack(counter, [], len(nums))
        return results

def main():
    nums = [1,1,2]
    my_object = Solution()        
    judgement = my_object.permute(nums)
    print(judgement)

if __name__ == "__main__":
   main()