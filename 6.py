N = int(input())

if N <= 10 ** 3 -1:
  print(N)

elif N <= 10 ** 4 -1:
  i = 1

elif N <= 10 ** 5 -1:
  i = 2

elif N <= 10 ** 6 -1:
  i = 3

elif N <= 10 ** 7 -1:
  i = 4

elif N <= 10 ** 8 -1:
  i = 5

elif N <= 10 ** 9 -1:
  i = 6


print(str(N)[:-i] + "0" * i)