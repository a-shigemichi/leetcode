from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Counts the number of good triplets in the array.
        
        A triplet (arr[i], arr[j], arr[k]) is good if:
        - 0 <= i < j < k < arr.length
        - |arr[i] - arr[j]| <= a
        - |arr[j] - arr[k]| <= b  
        - |arr[i] - arr[k]| <= c
        
        Args:
            arr: List[int] - The input array of integers
            a: int - Maximum allowed difference between arr[i] and arr[j]
            b: int - Maximum allowed difference between arr[j] and arr[k]
            c: int - Maximum allowed difference between arr[i] and arr[k]
            
        Returns:
            int - The number of good triplets
        """
        n = len(arr)
        count = 0
        
        # Try all possible triplets with i < j < k
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (abs(arr[i] - arr[j]) <= a and 
                        abs(arr[j] - arr[k]) <= b and 
                        abs(arr[i] - arr[k]) <= c):
                        count += 1

        return count
