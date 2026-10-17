class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Collect all starting cities into a set
        start_cities = {path[0] for path in paths}
        
        # Check every destination city
        for path in paths:
            destination = path[1]
            if destination not in start_cities:
                return destination