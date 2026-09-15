from collections import Counter
from typing import List
class Solution:
  def commonChars(self, words: List[str]) -> List[str]:
    min_freq = Counter(words[0])
    for word in words[1:]:
      word_freq = Counter(word)
      for char in min_freq:
        min_freq[char] = min(min_freq[char], word_freq[char])
    res = []
    for char, count in min_freq.items():
      res.extend([char] * count)
    return res