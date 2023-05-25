from typing import List

def partition(numbers: List[int], low: int, high: int) -> int:
  i = low - 1
  pivot = numbers[high]
  for j in range(low, high):
    if numbers[j] <= pivot:
      i += 1
      numbers[i], numbers[j] = numbers[j], numbers[i]
  numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
  return i+1