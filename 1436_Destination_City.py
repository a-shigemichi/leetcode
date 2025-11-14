from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        Find the destination city from a list of directed paths.
        
        Args:
            paths: A list of paths where each path is represented as [cityA, cityB]
                   indicating a direct path from cityA to cityB.
            
        Returns:
            The destination city that has no outgoing path.
        """
        outgoing = set()
        all_cities = set()
        
        for path in paths:
            outgoing.add(path[0])
            all_cities.add(path[0])
            all_cities.add(path[1])
        
        for city in all_cities:
            if city not in outgoing:
                return city
