from typing import List


class Solution:

  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k

    while left < right:
      mid = left + (right - left) // 2

      # Compare distances without abs() by leveraging sorted order:
      # x - arr[mid] > arr[mid + k] - x means arr[mid + k] is closer than arr[mid]
      if x - arr[mid] > arr[mid + k] - x:
        left = mid + 1
      else:
        right = mid

    return arr[left : left + k]