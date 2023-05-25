from __future__ import annotations
from typing import Any

#粒(リンク)を管理するクラス
class Node(object):
  def __init__(self, data: Any, next_node: Node = None):
    self.data = data
    self.next = next_node


#全体を管理するクラス
class LinkdeList(object):
  def __init__(self, head=None) -> None:
    self.head = head

  def append(self, data: Any) -> None:
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    
    last_node = self.head
    #一番右のノードを取ってきたい
    while last_node.next:
      last_node = last_node.next
    #一番右のノードに新しいノードを追加する
    last_node.next = new_node

  def insert(self, data: Any) -> None:
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def print(self) -> None:
    current_node = self.node
    while current_node:
      print(current_node.data)
      current_node = current_node.next

  def remove(self, data: Any) -> None:
    current_node = self.head
    if current_node and current_node.data == data:
      self.head = current_node.next
      current_node = None
      return
    
    previous_node = None
    while current_node and current_node.data != data:
      previous_node = current_node
      current_node = current_node.next

    if current_node is None:
      return
    
    previous_node.next = current_node.next
    current_node = None

  def reverse_iterative(self) -> None:
    previous_node = None
    current_node = self.head
    while current_node:
      next_node = current_node.next
      #くっつける作業 
      current_node.next = previous_node

      #現在のノードを保管しておく
      previous_node = current_node
      current_node = next_node
  
    self.head = previous_node

  def reverse_even(self) -> None:
    def _reverse_even(head: Node, previous_node: Node):
      if head is None:
        return None
      
      current_node = head
      while current_node and current_node.data % 2 == 0:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

      if current_node != head:
        head.next = current_node
        _reverse_even(current_node, None)
        return previous_node
      else:
        head.next = _reverse_even(head.next, head)
        return head
    
    self.head = _reverse_even(self.head, None)