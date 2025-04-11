from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        Find the lexicographically smallest string that can be obtained by swapping characters
        at the indices specified in the pairs array any number of times.
        
        Args:
            s (str): Input string
            pairs (List[List[int]]): Array of index pairs where characters can be swapped
            
        Returns:
            str: Lexicographically smallest possible string after swaps
        """
        n = len(s)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for a, b in pairs:
            union(a, b)
        
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        result = list(s)
        for indices in groups.values():
            characters = [s[i] for i in indices]
            characters.sort()
            indices.sort()
            for i, c in zip(indices, characters):
                result[i] = c
        
        return ''.join(result)
    