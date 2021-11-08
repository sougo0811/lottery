#抽選
import math
import random

N = 10
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

#print(lottery_A())
#print(lottery_B())

