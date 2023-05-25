class Node(object):
  def __init__(self, value: int) -> None:
    self.value = value
    self.left = Node
    self.right = Node

def insert(node: Node, value: int) -> Node:
  if node is None:
    return Node(value)

  if value < node.value:
    node.left = insert(node.left, value)
  else:
    node.right = insert(node.right, value)
  return node

def search(node: Node, value: int) -> bool:
  if node is None:
    return False

  if node.value == value:
    return True
  elif node.value > value:
    return search(node.left, value)
  elif node.value < value:
    return search(node.right, value)

def min_value(node: Node) -> Node:
  current = node
  while current.left is not None:
    current = current.left
  return current


def remove(node: Node, value: int) -> Node:
  if node is None:
    return node
  
  #value探し
  if value < node.value:
    node.left = remove(node.left, value)
  elif value > node.value:
    node.right = remove(node.right, value)
  #valueが見つかった時の処理
  else:
    #leftが無かったら、rightを上に持ってくる
    if node.left is None:
      return node.right
    #rightが無かったら、leftを上に持ってくる
    elif node.right is None:
      return node.left
    
    #left,rightどっちもあった時に、right側のleftの一番下のnodeを上に持ってくる -> 良い感じになる
    temp = min_value(node.right)
    node.value = temp.value
    node.right = remove(node.right, temp.value)
  return node

  