from __future__ import annotations
from typing import Any, Counter, NewType, Optional


class Node(object):
  def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
    self.data = data
    self.next = next_node
    self.prev = prev_node


class DoublyLinkdeList(object):
  def __init__(self, head: Node = None) -> None:
    self.head = head

  def append(self, data: Any) -> None:
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    current_node = self.head
    while current_node.next:
      current_node = current_node.next
    current_node.next = new_node
    new_node.prev = current_node

  def insert(self, data: Any) -> None:
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    self.head.prev = new_node
    new_node.next = self.head
    self.head = new_node

  def print(self) -> None:
    current_node = self.head
    
    while current_node:
      print(current_node.data)
      current_node = current_node.next

  def remove(self, data: Any) -> None:
    current_node = self.head

    #先頭を削除する
    if current_node and current_node.data == data:
      #次が無い
      if current_node.next is None:
        current_node = None
        self.head = None
        return
      else:
        #次もある
        next_node = current_node.next
        next_node.prev = None
        current_node = None
        self.head = next_node
        return
    
    #途中を削除する
    #削除したいnodeを取得してからループを抜ける
    while current_node and current_node.data != data:
      current_node = current_node.next

    #削除するやつが無い時 current.nextは無いから current_nodeはNoneになる
    if current_node is None:
      return

    #削除するやつが最後の時
    if current_node.next is None:
      prev = current_node.prev
      prev.next = None
      current_node = None
      return
    else: #途中にある場合
      next_node = current_node.next
      prev_node = current_node.prev
      prev_node.next = next_node
      next_node.prev = prev_node
      current_node = None
      return

  def reverse_iterative(self) -> None:
    previous_node = None
    current_node = self.head
    while current_node:
      previous_node = current_node.prev
      current_node.prev = current_node.next
      current_node.next = previous_node

      current_node = current_node.prev
    
    if previous_node:
      self.head = previous_node.prev

  def reverse_recursive(self) -> None:
    def _reverse_recursive(current_node: Node) -> Optional[Node]:
      if not current_node:
        return None
      
      previous_node = current_node.prev
      current_node.prev = current_node.next
      current_node.next = previous_node

      if current_node.prev is None:
        return current_node
      
      return _reverse_recursive(current_node.prev)

    #呼び出す最初のプログラム
    self.head = _reverse_recursive(self.head)

  def sort(self) -> None:
    if self.head is None:
      return 

    current_node = self.head
    #次（右側）がなくなったらループ終了→どうなったらループ終了かを考える
    while current_node.next:
      next_node = current_node.next
      while next_node:
        if current_node.data > next_node:
          current_node.data, next_node.data= next_node.data, current_node.data
        next_node = next_node.next
      
      current_node = current_node.next