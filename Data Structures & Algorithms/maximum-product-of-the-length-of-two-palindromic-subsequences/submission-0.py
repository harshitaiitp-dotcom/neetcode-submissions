class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        pali = {}
        
        # Step 1: Find all palindromic subsequences and store their lengths by bitmask
        for mask in range(1, 1 << n):
            subseq = []
            for i in range(n):
                if (mask & (1 << i)):
                    subseq.append(s[i])
            
            # Check if the subsequence is a palindrome
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)
        
        # Step 2: Find two disjoint palindromic subsequences with the maximum product
        max_prod = 0
        pali_masks = list(pali.keys())
        
        for i in range(len(pali_masks)):
            for j in range(i + 1, len(pali_masks)):
                mask1 = pali_masks[i]
                mask2 = pali_masks[j]
                
                # Check if the two masks are disjoint (no shared indices)
                if (mask1 & mask2) == 0:
                    max_prod = max(max_prod, pali[mask1] * pali[mask2])
                    
        return max_prod