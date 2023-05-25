from typing import Any

class Queue:
  def __init__(self) -> None:
    self.queue = []

  def enqueue(self, data: Any) -> None:
    self.queue.append(data)

  def dequeue(self) -> Any:
    if self.queue:
      self.queue.pop(0)