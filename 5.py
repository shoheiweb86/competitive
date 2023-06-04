def f(s):
    lst = s.split()
    return lst[0], int(lst[1])


N = int(input())
input_list = [f(input()) for i in range(N)]


small_age = input_list[0][1]
small_age_index = 0

#一番年齢が小さい人のindexを取得
for i in range(N):
  if input_list[i][1] < small_age:
    small_age = input_list[i][1]
    small_age_index = i

for i in range(small_age_index, N):
  print(input_list[i][0])

for i in range(0, small_age_index):
  print(input_list[i][0])