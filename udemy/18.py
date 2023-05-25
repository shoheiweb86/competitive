from collections import Counter
import heapq
from typing import List

def top_n_with_heap(words: List[str], n: int) -> List[str]:
  couter_word = Counter(words)
  #(a, b)はタプルを作成してる リスト内包括は、タプルも作成できるってこと
  data = [(-couter_word[word], word) for word in couter_word]
  heapq.heapify(data)
  #タプルだから、[1]にしてwordを表示してる
  return [heapq.heappop(data)[1] for _ in range(n)]


if __name__ == '__main__':
  w = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python','java', 'java']
  print(top_n_with_heap(w, 3))
