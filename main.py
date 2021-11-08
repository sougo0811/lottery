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
  if len(your_selects) >= 1 and select_flg == True:
    candidate_number = []
    candidate_number.extend(lottery_A())
    candidate_number.extend(lottery_B())
    lottery_number = random.choice(candidate_number)
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
      Happy_label = tkinter.Label(tab_out, font=("sans-serif", 30), text= "当選！", foreground="red", background="white")
      Happy_label.place(x = 420, y = 150)
      print("当選！")
    else:
      normal_label = tkinter.Label(tab_out, font=("sans-serif", 30), text= "落選", foreground="blue", background="white")
      normal_label.place(x = 450, y = 150)
      print("落選")
    lottery_check_flg = False
  else:
    messagebox.showwarning("現在の状況では確認できません", "抽選確認は、抽選後に一回だけできます")
    print("抽選後に押してください")

your_selects = []
with open("select_number.txt", mode="w", encoding="utf-8") as fw:
  fw.write("あなたの抽選番号\n")
select_flg = True
lottery_check_flg = True
n = 15
root = tkinter.Tk()
root.title("宝くじ")
root.geometry("600x450")

notebook = ttk.Notebook(root)
tab_in = tkinter.Frame(notebook)
tab_out = tkinter.Frame(notebook)
notebook.add(tab_in, text="入力")
notebook.add(tab_out, text="出力")

entry = tkinter.Entry(tab_in, width=6, font=("sans-serif", 30))
entry.place(x=230, y=140)

button = tkinter.Button(tab_in, height= 2, width = 10, text="追加", command=click_btn)
#button.bind("<Return>", lambda event: click_btn)
button.place(x=250, y=200)

button = tkinter.Button(tab_in, height= 2, width = 10, text="抽選", command=lottery_btn)
button.place(x=250, y=250)

button = tkinter.Button(tab_in, height= 2, width = 10, text="当選確認", command=lottery_check_btn)
button.place(x=250, y=300)

notebook.pack(expand=True, fill='both', padx=10, pady=10)


select_canvas = tkinter.Canvas(tab_out, bg="white")
select_canvas.place(x=0, y=10, width=200, height=390)

bar_y = tkinter.Scrollbar(select_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=select_canvas.yview)
select_canvas.config(yscrollcommand=bar_y.set)
select_canvas.config(scrollregion=(0, 0, 0, 2000))

select_canvas.create_text(90, 10, font=("sans-serif", 10), text="あなたの入力した数字")

result_canvas = tkinter.Canvas(tab_out, bg="white")
result_canvas.place(x=200, y=10, width=200, height=390)

bar_y = tkinter.Scrollbar(result_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=result_canvas.yview)
result_canvas.config(yscrollcommand=bar_y.set)
result_canvas.config(scrollregion=(0, 0, 0, 2000))

result_canvas.create_text(90, 10, font=("sans-serif", 10), text="当選番号")

root.mainloop()

#your_select = list(map(int,input("6桁の数字を入力してください：").split()))




