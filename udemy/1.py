from typing import List


def cooktail_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  swapped = True
  start = 0
  end = len_numbers - 1
  while swapped:
    swapped = False
    for i in range(start, end):
      if numbers[i] > numbers[i+1]:
        numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
        swapped = True

    if not swapped:
      break

    swapped = False
    end = end - 1
    
    for i in range(end-1, start-1, -1):
      if numbers[i] > numbers[i+1]:
        numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
        swapped = True
        print(i)
        
    start = start + 1

  return numbers


import random
nums = [random.randint(0, 1000) for i in range(6)]
print(cooktail_sort(nums))