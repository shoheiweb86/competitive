from typing import List, Tuple, Optional


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
  cache = set()
  for num in numbers:
    val = target - num
    if val in cache:
      return val, num
    cache.add(num)

def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
  sum_numbers = sum(numbers)
  # if numbers_sum % 2 != 0:
  #   return
  # numbers_half_sum = int(numbers_sum / 2)

  half_sum, remainder = divmod(sum_numbers, 2)
  if remainder != 0:
    return  

  cache = set()
  for num in numbers:
    val = half_sum - num
    if val in cache:
      return val, num
    cache.add(num)


l = [11, 2, 5, 9, 10, 3]
t = 12
print(get_pair(l, t))
print(get_pair_half_sum(l))