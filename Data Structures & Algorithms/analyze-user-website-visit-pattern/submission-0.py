from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Combine the inputs and sort them chronologically by timestamp
        visits = sorted(zip(username, timestamp, website), key=lambda x: x[1])
        
        # Step 2: Group visited websites by user in chronological order
        user_history = defaultdict(list)
        for u, t, w in visits:
            user_history[u].append(w)
            
        # Step 3: Count the number of UNIQUE users who visited each 3-website pattern
        pattern_count = defaultdict(int)
        
        for u, websites in user_history.items():
            # Generate all unique 3-website combinations (subsequences) for this user
            user_patterns = set(combinations(websites, 3))
            
            for pattern in user_patterns:
                pattern_count[pattern] += 1
                
        # Step 4: Find the pattern with the maximum score.
        # Ties are broken lexicographically using (-score, pattern).
        best_pattern = min(
            pattern_count.keys(),
            key=lambda p: (-pattern_count[p], p)
        )
        
        return list(best_pattern)