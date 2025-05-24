from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Find the prefix common array of two permutations using the set approach.
        
        A prefix common array C is defined such that C[i] is equal to the count of numbers 
        that are present at or before the index i in both A and B.
        
        Args:
            A: A permutation of integers from 1 to n
            B: A permutation of integers from 1 to n
            
        Returns:
            The prefix common array of A and B
        """
        n = len(A)

        seen_a = set()
        seen_b = set()

        result = [0] * n
        
        for i in range(n):
            seen_a.add(A[i])
            seen_b.add(B[i])

            common_count = len(seen_a.intersection(seen_b))

            result[i] = common_count
            
        return result
    