class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Initial penalty if shop closes at hour 0 (all 'Y' incur a penalty)
        current_penalty = customers.count('Y')
        min_penalty = current_penalty
        best_hour = 0
        
        for i, ch in enumerate(customers):
            if ch == 'Y':
                current_penalty -= 1
            else: # ch == 'N'
                current_penalty += 1
                
            # Update min_penalty and best_hour if a strictly lower penalty is found
            # (We use '<' to ensure we keep the earliest hour)
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_hour = i + 1
                
        return best_hour