#宝くじ

import random
import tkinter
import tkinter.ttk as ttk
from tkinter import messagebox
from lottery import lottery_A,lottery_B
#import sys

def check(your_select):
  flg = 0
  if len(str(your_select)) == 6:
    flg = 0
  else:
    flg += 1
  return flg

def click_btn():
  global your_selects
  global check
  global n
  try:
    your_select = int(entry.get())
  except ValueError:
    entry.delete(0, tkinter.END)
    messagebox.showerror("入力値が正しくありません", "6桁の数字を入力してください")
    print("情報が正しくありません")
  else:
    check_ans = check(your_select)
    if check_ans == 0:
      your_selects.append(your_select)
      entry.delete(0, tkinter.END)
      n += 20
      select_canvas.create_text(90, n, font=("sans-serif", 10), text=your_select)
      with open("select_number.txt",mode="a") as f:
        f.write(str(your_select)+"\n")
    else:
      entry.delete(0, tkinter.END)
      messagebox.showerror("入力値が正しくありません", "6桁の数字を入力してください")
      print("情報が正しくありません")
    return your_selects

def lottery_btn():
  global your_selects
  global select_flg
  global candidateA_flg
  global candidateB_flg
  global candidate_numbers
  if len(your_selects) >= 1 and select_flg == True and candidateA_flg == True and candidateB_flg == True:
    candidate_numbers.extend(lottery_A())
    candidate_numbers.extend(lottery_B())
    lottery_number = random.choice(candidate_numbers)
    result_canvas.create_text(90, 30, font=("sans-serif", 10), text=lottery_number)
    with open("lottery_number.txt", mode="w", encoding="utf-8") as f:
      f.write("当選番号\n" + str(lottery_number))
    print("抽選しました")
    select_flg = False
    candidateA_flg = False
    candidateB_flg = False
  elif len(your_selects) >= 1 and select_flg == True and candidateA_flg == False and candidateB_flg == True:
    candidate_numbers.extend(lottery_B())
    lottery_number = random.choice(candidate_numbers)
    result_canvas.create_text(90, 30, font=("sans-serif", 10), text=lottery_number)
    with open("lottery_number.txt", mode="w", encoding="utf-8") as f:
      f.write("当選番号\n" + str(lottery_number))
    print("抽選しました")
    select_flg = False
    candidateB_flg = False
  elif len(your_selects) >= 1 and select_flg == True and candidateA_flg == True and candidateB_flg == False:
    candidate_numbers.extend(lottery_A())
    lottery_number = random.choice(candidate_numbers)
    result_canvas.create_text(90, 30, font=("sans-serif", 10), text=lottery_number)
    with open("lottery_number.txt", mode="w", encoding="utf-8") as f:
      f.write("当選番号\n" + str(lottery_number))
    print("抽選しました")
    select_flg = False
    candidateA_flg = False
  elif len(your_selects) >= 1 and select_flg == True and candidateA_flg == False and candidateB_flg == False:
    lottery_number = random.choice(candidate_numbers)
    result_canvas.create_text(90, 30, font=("sans-serif", 10), text=lottery_number)
    with open("lottery_number.txt", mode="w", encoding="utf-8") as f:
      f.write("当選番号\n" + str(lottery_number))
    print("抽選しました")
    select_flg = False
  else:
    messagebox.showwarning("現在の状況では抽選できません", "抽選番号の未入力及び複数回の抽選はできません")
    print("抽選番号の未入力及び複数回の抽選はできません")

def lottery_check_btn():
  your_list = []
  global select_flg
  global lottery_check_flg
  if lottery_check_flg == True and select_flg == False:
    with open("select_number.txt", mode="r", encoding="utf-8") as f:
      next(f)
      for i, s in enumerate(f, start=2):
        your_list.append(int(s))
    with open("lottery_number.txt", mode="r", encoding="utf-8") as f:
      next(f)
      lottery_num = f.read()
      lottery_num = int(lottery_num)
    if lottery_num in your_list:
      Happy_label = tkinter.Label(tab_home, font=("sans-serif", 30), text= "当選！", foreground="red", background="white")
      Happy_label.place(x = 53, y = 40)
      print("当選！")
    else:
      normal_label = tkinter.Label(tab_home, font=("sans-serif", 30), text= "落選", foreground="blue", background="white")
      normal_label.place(x = 53, y = 40)
      print("落選")
    lottery_check_flg = False
  else:
    messagebox.showwarning("現在の状況では確認できません", "抽選確認は、抽選後に一回だけできます")
    print("抽選後に押してください")

def candidateA():
  global m
  global your_selects
  global select_flg
  global candidateA_flg
  global candidate_numbers
  if candidateA_flg == True and select_flg == True:
    candidate_numbers.extend(lottery_A())
    for candidate_number in candidate_numbers:
      m += 20
      result_canvas.create_text(90, m, font=("sans-serif", 10), text=candidate_number)
      with open("select_number.txt",mode="a") as f:
        f.write(candidate_number+"\n")
    print("抽選候補を出しました")
    candidateA_flg = False
  else:
    messagebox.showwarning("現在の状況では抽選できません", "抽選後の候補抽選及び複数回の候補抽選はできません")
    print("抽選後の候補抽選及び複数回の候補抽選はできません")

def candidateB():
  global m
  global your_selects
  global select_flg
  global candidateB_flg
  global candidate_numbers
  if candidateB_flg == True and select_flg == True:
    candidate_numbers.extend(lottery_B())
    for candidate_number in candidate_numbers:
      m += 20
      result_canvas.create_text(90, m, font=("sans-serif", 10), text=candidate_number)
      with open("select_number.txt",mode="a") as f:
        f.write(candidate_number+"\n")
    print("抽選候補を出しました")
    candidateB_flg = False
  else:
    messagebox.showwarning("現在の状況では抽選できません", "抽選後の候補抽選及び複数回の候補抽選はできません")
    print("抽選後の候補抽選及び複数回の候補抽選はできません")

your_selects = []
candidate_numbers = []
with open("select_number.txt", mode="w", encoding="utf-8") as fw:
  fw.write("あなたの抽選番号\n")
with open("candidate_number.txt", mode="w", encoding="utf-8") as fw:
  fw.write("抽選候補番号\n")
select_flg = True
lottery_check_flg = True
candidateA_flg = True
candidateB_flg = True
n = 15
m = 15
root = tkinter.Tk()
root.title("宝くじ")
root.geometry("600x450")

notebook = ttk.Notebook(root)
tab_home = tkinter.Frame(notebook)
tab_out = tkinter.Frame(notebook)
tab_lottery = tkinter.Frame(notebook)
notebook.add(tab_home, text="ホーム")
notebook.add(tab_out, text="出力")
notebook.add(tab_lottery, text="抽選")

entry = tkinter.Entry(tab_home, width = 6, font=("sans-serif", 30))
entry.place(x=35, y=110)

button_add = tkinter.Button(tab_home, height = 3, width = 15, text="追加", command=click_btn)
#button.bind("<Return>", lambda event: click_btn)
button_add.place(x=40, y=180)

button_lot = tkinter.Button(tab_home, height = 3, width = 15, text="抽選", command=lottery_btn)
button_lot.place(x=40, y=240)

button_ch = tkinter.Button(tab_home, height = 3, width = 15, text="当選確認", command=lottery_check_btn)
button_ch.place(x=40, y=300)

button_canA = tkinter.Button(tab_lottery, height = 2, width = 10, text="抽選方法A", command=candidateA)
button_canA.place(x=50, y=50)

button_canB = tkinter.Button(tab_lottery, height = 2, width = 10, text="抽選方法B", command=candidateB)
button_canB.place(x=150, y=50)

notebook.pack(expand=True, fill='both', padx=10, pady=10)


select_canvas = tkinter.Canvas(tab_home, bg="white")
select_canvas.place(x=190, y=10, width=190, height=390)

bar_y = tkinter.Scrollbar(select_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=select_canvas.yview)
select_canvas.config(yscrollcommand=bar_y.set)
select_canvas.config(scrollregion=(0, 0, 0, 2000))

select_canvas.create_text(90, 10, font=("sans-serif", 10), text="あなたの入力した数字")

candidate_canvas = tkinter.Canvas(tab_out, bg="white")
candidate_canvas.place(x=190, y=10, width=190, height=390)

bar_y = tkinter.Scrollbar(candidate_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=candidate_canvas.yview)
candidate_canvas.config(yscrollcommand=bar_y.set)
candidate_canvas.config(scrollregion=(0, 0, 0, 2000))

candidate_canvas.create_text(90, 10, font=("sans-serif", 10), text="候補番号")

result_canvas = tkinter.Canvas(tab_home, bg="white")
result_canvas.place(x=380, y=10, width=190, height=390)

bar_y = tkinter.Scrollbar(result_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=result_canvas.yview)
result_canvas.config(yscrollcommand=bar_y.set)
result_canvas.config(scrollregion=(0, 0, 0, 2000))

result_canvas.create_text(90, 10, font=("sans-serif", 10), text="当選番号")

root.mainloop()

#your_select = list(map(int,input("6桁の数字を入力してください：").split()))




