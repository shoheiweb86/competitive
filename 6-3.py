N = int(input())
S = input()


def check_winner(N, S):
  T = 0
  A = 0

  #偶数の場合
  if N % 2 == 0:
    for s in S:
      if s == 'T':
        T += 1
      else:
        A += 1

      if T == N / 2:
        return 'T'
      elif A == N / 2:
        return 'A'
    

  #奇数の場合
  if N % 2 != 0:
    for s in S:
      if s == 'T':
        T += 1
      else: A += 1

      if T == N // 2 + 1:
        return 'T'
      elif A == N // 2 + 1:
        return 'A'


print(check_winner(N, S))