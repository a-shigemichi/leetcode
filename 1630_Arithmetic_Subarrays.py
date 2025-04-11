from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        Check if each subarray defined by the ranges [l[i], r[i]] can be rearranged 
        to form an arithmetic sequence.
        
        Args:
            nums (List[int]): Array of integers
            l (List[int]): Array of left bounds for each query range
            r (List[int]): Array of right bounds for each query range
            
        Returns:
            List[bool]: List where answer[i] indicates if the subarray nums[l[i]]...nums[r[i]]
                       can be rearranged to form an arithmetic sequence
        """
        m = len(l)
        answer = []
        
        for i in range(m):
            subarray = nums[l[i]:r[i] + 1]
            answer.append(self.canFormArithmeticSequence(subarray))
        
        return answer
    
    def canFormArithmeticSequence(self, arr):
        if len(arr) <= 1:
            return True
        
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        
        return True
    