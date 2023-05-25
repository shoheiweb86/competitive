from typing import List

def insertion_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)

  for i in range(1, len_numbers):
    tmp = numbers[i]
    j = i -1
    while j >= 0 and numbers[j] > tmp:
      numbers[j+1] = numbers[j]
      j -= 1

    numbers[j+1] = tmp
  
  return numbers

import random
nums = [random.randint(0,1000) for i in range(10)]
print(insertion_sort(nums))
