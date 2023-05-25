import hashlib

class HashTable(object):
  def __init__(self, size=10) -> None:
    self.size = size
    self.table = [[] for _ in range(size)]

  def hash(self, key) -> int:
    return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

  def add(self, key, value) -> None:
    #index番号を取得
    index = self.hash(key)
    #[[], [index], [ここ]]を回してる
    for data in self.table[index]:
      #data[0]はsnsとか、カテゴリー
      if data[0] == key:
        #既に存在しているカテゴリーなら、valueを上書きする
        data[1] = value
        break
      else:
        #存在していないカテゴリーなら、カテゴリーを作ってvalueも入れる
        self.table[index].append([key, value])

