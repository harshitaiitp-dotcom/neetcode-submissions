class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        
        # Populate the difference array
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val
            
        # Compute prefix sums to get the net shift for each character
        current_shift = 0
        result = []
        
        for i in range(n):
            current_shift += diff[i]
            # Map character to 0-25, apply shift, handle negative wrapping with modulo 26, and convert back to char
            original_char_val = ord(s[i]) - ord('a')
            new_char_val = (original_char_val + current_shift) % 26
            result.append(chr(ord('a') + new_char_val))
            
        return "".join(result)