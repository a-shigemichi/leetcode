class Solution:
    def findErrorNums(nums: list[int]) -> list[int]:
        """
        Find the number that appears twice and the missing number in the array.
        
        Args:
            nums (list[int]): Array containing numbers from 1 to n with one duplicate
                and one missing number
                
        Returns:
            list[int]: [duplicated_number, missing_number]

        """
        n = len(nums)
        num_set = set()
        duplicate = 0
        
        for num in nums:
            if num in num_set:
                duplicate = num
            num_set.add(num)

        for i in range(1, n + 1):
            if i not in num_set:
                return [duplicate, i]
                
        return []
    