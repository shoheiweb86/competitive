from typing import List, NewType
IndexNum = NewType('IndexNum', int)


def linear_search(numbers: List[int], value: int) -> IndexNum:
  for i in range(0, len(numbers)):
    if numbers[i] == value:
      return i
  return -1


def binary_search(numbers: List[int], value: int) -> IndexNum:
  left, right = 0, len(numbers) - 1
  while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == value:
      return numbers[mid]
    elif numbers[mid] < value:
      left = mid + 1
    else:
      right = mid -1
  return -1

import random
nums = [random.randint(0,10) for _ in range(10)]
print(binary_search(nums,8))