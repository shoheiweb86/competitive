from typing import Tuple


def validate_format(chars: str) -> bool:
  lookup = {'{': '}', '[': ']', '(': ')'}
  stack = []
  for char in chars:
    if char == lookup.keys():
      stack.append(lookup[char])

    if char == lookup.values():
      if not stack:
        return False
      if char != stack.pop():
        return False

    if stack:
      return False
    
    return True