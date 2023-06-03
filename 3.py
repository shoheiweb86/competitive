N = int(input())
S = input()
T = input()

temp = "No"
for s, t in zip(S, T):
    #同じ文字の場合
    if s == t:
      temp = "Yes"
    #1,l,0,oの場合
    elif s == "1" and t == "l":
      temp = "Yes"
    elif s == "0" and t == "o":
      temp = "Yes"
    elif s ==  "l" and t == "1":
      temp = "Yes"
    elif s ==  "o" and t == "0":
      temp = "Yes"
    else:
      temp = "No"
      break
      

print(temp)
