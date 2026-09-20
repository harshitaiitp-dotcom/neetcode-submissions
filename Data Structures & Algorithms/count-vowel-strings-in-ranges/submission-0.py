class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        prefix_sum = [0] * (n + 1)       
        for i in range(n):
            word = words[i]
            is_vowel_string = 1 if (word[0] in vowels and word[-1] in vowels) else 0
            prefix_sum[i + 1] = prefix_sum[i] + is_vowel_string           
        res = []
        for l, r in queries:
            res.append(prefix_sum[r + 1] - prefix_sum[l])            
        return res