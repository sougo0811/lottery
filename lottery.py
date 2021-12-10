#抽選
import random

N = 20
def lottery_A():
  win_numbers_A = []
  for i in range(N):
    win_num = random.randint(100000,999999)
    win_numbers_A.append(win_num)
  return win_numbers_A

def lottery_B():
  win_numbers_B = []
  for i in range(N):
    win_num = []
    one_flg = True
    for j in range(6):
      if one_flg == True:
        select_num = random.randint(1,9)
        win_num.append(select_num)
        one_flg = False
      else:
        select_num = random.randint(0,9)
        win_num.append(select_num)
    win_num = map(str,win_num)
    win_num = int(''.join(win_num))
    win_numbers_B.append(win_num)
  return win_numbers_B

def lottery_test():
  win_numbers_test = [123456,111111,222222,333333,444444,555555,666666,777777,888888,999999]
  return win_numbers_test

#print(lottery_A())
#print(lottery_B())
#print(lottery_test())