class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Pad string with virtual bounds to simplify edge conditions
        d = 'L' + dominoes + 'R'
        res = []
        l = 0
        
        for r in range(1, len(d)):
            if d[r] == '.':
                continue
            
            count = r - l - 1  # Number of '.' between l and r
            
            if l > 0:
                res.append(d[l])
            
            if d[l] == d[r]:
                # Case 1 & 2: Same forces ('L...L' or 'R...R')
                res.append(d[l] * count)
            elif d[l] == 'L' and d[r] == 'R':
                # Case 3: Forces point away ('L...R') -> remain dots
                res.append('.' * count)
            elif d[l] == 'R' and d[r] == 'L':
                # Case 4: Forces point inwards ('R...L')
                half = count // 2
                res.append('R' * half)
                if count % 2 == 1:
                    res.append('.')  # Middle balanced domino
                res.append('L' * half)
            
            l = r
            
        return "".join(res)