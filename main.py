#宝くじ

import random
import tkinter
import tkinter.ttk as ttk
from tkinter import messagebox
from lottery import lottery_A,lottery_B,lottery_test
#import time
#import sys

#ノーマルモード
def normal_btn():
  global develop_flg
  develop_flg = False
  print("ノーマルモード")
  
#開発モード
def develop_btn():
  global develop_flg
  develop_flg = True
  print("開発モード")

#ホーム関数
def limit_char(string):
    return len(string) <= 6

def check(your_select):
  global your_selects
  flg_A = True
  flg_B = True
  if len(str(your_select)) != 6:
    flg_A = False
  if your_select in your_selects:
    flg_B = False
  return [flg_A,flg_B]

def numcheck_btn():
  global your_selects
  global check
  global n
  global select_flg
  
  if select_flg == True:
    try:
      your_select = int(entry.get())
    except ValueError:
      entry.delete(0, tkinter.END)
      messagebox.showerror("入力値が正しくありません", "6桁の数字を入力してください")
      print("入力値が正しくありません")
    else:
      check_ans = check(your_select)
      if check_ans[0] == True and check_ans[1] == True:
        your_selects.append(your_select)
        entry.delete(0, tkinter.END)
        n += 20
        select_canvas.create_text(90, n, font=("sans-serif", 10), text=your_select)
        with open("./text_file/select_number.txt",mode="a") as f:
          f.write(str(your_select)+"\n")
      elif check_ans[0] == False and check_ans[1] == True:
        entry.delete(0, tkinter.END)
        messagebox.showerror("入力桁数が正しくありません", "6桁の数字を入力してください")
        print("入力桁数が正しくありません")
      elif check_ans[0] == True and check_ans[1] == False:
        entry.delete(0, tkinter.END)
        messagebox.showerror("入力番号が被っています", "別の番号を入力してください")
        print("入力番号が被っています")
      else:
        entry.delete(0, tkinter.END)
        messagebox.showerror("存在し得ないエラーです", "このエラー文は出てきてはいけません")
        print("存在し得ないエラー")
      return your_selects
  else:
    entry.delete(0, tkinter.END)
    messagebox.showwarning("現在の状況では追加できません", "抽選後の番号の追加はできません")
    print("抽選後の番号の追加はできません")

def lottery_btn():
  global your_selects
  global select_flg
  global develop_flg
  global candidate_numbers
  global m
  if len(your_selects) >= 1 and select_flg == True:
    if develop_flg == False:
      candidate_numbers.extend(lottery_A())
      candidate_numbers.extend(lottery_B())
      lottery_numbers = random.sample(candidate_numbers,num_win)
    elif develop_flg == True:
      candidate_numbers.extend(lottery_test())
      lottery_numbers = random.sample(candidate_numbers,num_win-1)
      lottery_numbers.append(int(123456))
    for lottery_number in lottery_numbers:
      m += 20
      result_canvas.create_text(90, m, font=("sans-serif", 10), text=lottery_number)
      one_canvas.create_text(90, m, font=("sans-serif", 10), text=list(str(lottery_number)[0:6:]))
      two_canvas.create_text(90, m, font=("sans-serif", 10), text=list(str(lottery_number)[1:6:]))
      three_canvas.create_text(90, m, font=("sans-serif", 10), text=list(str(lottery_number)[2:6:]))
      with open("./text_file/lottery_number.txt", mode="a", encoding="utf-8") as f:
        f.write(str(lottery_number)+"\n")
      lottery_number = list(str(lottery_number))
      with open("./text_file/win_one.txt", mode="a", encoding="utf-8") as f:
        win_one = "".join(lottery_number[0:6:])
        f.write(str(win_one)+"\n")
      with open("./text_file/win_two.txt", mode="a", encoding="utf-8") as f:
        win_two = "".join(lottery_number[1:6:])
        f.write(str(win_two)+"\n")
      with open("./text_file/win_three.txt", mode="a", encoding="utf-8") as f:
        win_three = "".join(lottery_number[2:6:])
        f.write(str(win_three)+"\n")
      #print(lottery_number)
      
    print("抽選しました")
    select_flg = False
  else:
    messagebox.showwarning("現在の状況では抽選できません", "抽選番号の未入力及び複数回の抽選はできません")
    print("抽選番号の未入力及び複数回の抽選はできません")

def lottery_check_btn():
  #your_list = []
  your_one = []
  your_two = []
  your_three = []
  #lottery_nums = []
  win_ones = []
  win_twos = []
  win_threes = []
  global select_flg
  global lottery_check_flg
  global lottey_label
  if lottery_check_flg == True and select_flg == False:
    one_canvas.delete("all")
    two_canvas.delete("all")
    three_canvas.delete("all")
    one_canvas.create_text(90, 10, font=("sans-serif", 10), text="1等賞")
    two_canvas.create_text(90, 10, font=("sans-serif", 10), text="2等賞")
    three_canvas.create_text(90, 10, font=("sans-serif", 10), text="3等賞")
    with open("./text_file/select_number.txt", mode="r", encoding="utf-8") as f:
      next(f)
      for i, s in enumerate(f, start=2):
        #your_list.append(s)
        your_one.append("".join(list(s[0:6:])))
        your_two.append("".join(list(s[1:6:])))
        your_three.append("".join(list(s[2:6:])))
      your_one = list(set(your_one))
      your_two = list(set(your_two))
      your_three = list(set(your_three))
    with open("./text_file/lottery_number.txt", mode="r", encoding="utf-8") as f:
      next(f)
      for i, s in enumerate(f, start=2):
        win_ones.append(s[0:6:])
        win_twos.append(s[1:6:])
        win_threes.append(s[2:6:])
      win_ones = list(set(win_ones))
      win_twos = list(set(win_twos))
      win_threes = list(set(win_threes))
    win_cnt = 0
    win_one_cnt = 0
    win_two_cnt = 0
    win_three_cnt = 0
    m = 15
    for win_one in win_ones:
      m += 20
      if win_one in your_one:
        win_cnt += 1
        win_one_cnt += 1
        one_canvas.create_text(90, m, font=("sans-serif", 10), fill="red", text=list(str(win_one)))
      else:
        one_canvas.create_text(90, m, font=("sans-serif", 10), fill="blue", text=list(str(win_one)))
    m = 15
    for win_two in win_twos:
      m += 20
      if win_two in your_two:
        win_cnt += 1
        win_two_cnt += 1
        two_canvas.create_text(90, m, font=("sans-serif", 10), fill="red", text=list(str(win_two)))
      else:
        two_canvas.create_text(90, m, font=("sans-serif", 10), fill="blue", text=list(str(win_two)))
    m = 15
    for win_three in win_threes:
      m += 20
      if win_three in your_three:
        win_cnt += 1
        win_three_cnt += 1
        three_canvas.create_text(90, m, font=("sans-serif", 10), fill="red", text=list(str(win_three)))
      else:
        three_canvas.create_text(90, m, font=("sans-serif", 10), fill="blue", text=list(str(win_three)))
    if win_cnt != win_one_cnt + win_two_cnt + win_three_cnt:
      messagebox.showerror("エラー", "不正抽選の可能性があります")
      print("エラー")
    if win_cnt >= 1:
      lottey_label = tkinter.Label(tab_home, font=("sans-serif", 30), text= "当選！", foreground="red", background="white")
      lottey_label.place(x = 35, y = 30)
      print("当選！")
    else:
      lottey_label = tkinter.Label(tab_home, font=("sans-serif", 30), text= "落選", foreground="blue", background="white")
      lottey_label.place(x = 53, y = 30)
      print("落選")
    lottery_check_flg = False
    print("当選数"+str(win_cnt))
  else:
    messagebox.showwarning("現在の状況では確認できません", "抽選確認は、抽選後に一回だけできます")
    print("抽選後に押してください")


def reset_btn():
  global your_selects
  global select_flg
  global candidate_numbers
  global lottery_check_flg
  global lottey_label
  global n
  global m
  #global num_win
  
  n = 15
  m = 15
  #num_win = 10
  your_selects = []
  select_flg = True
  candidate_numbers = []
  lottery_check_flg = True
  entry.delete(0, tkinter.END)
  with open("./text_file/select_number.txt", mode="w", encoding="utf-8") as fw:
    fw.write("あなたの抽選番号\n")
  with open("./text_file/lottery_number.txt", mode="w", encoding="utf-8") as fw:
    fw.write("抽選番号\n")
  with open("./text_file/win_one.txt", mode="w", encoding="utf-8") as fw:
    fw.write("1等賞\n")
  with open("./text_file/win_two.txt", mode="w", encoding="utf-8") as fw:
    fw.write("2等賞\n")
  with open("./text_file/win_three.txt", mode="w", encoding="utf-8") as fw:
    fw.write("3等賞\n")
  lottey_label.place_forget()
  select_canvas.delete("all")
  result_canvas.delete("all")
  one_canvas.delete("all")
  two_canvas.delete("all")
  three_canvas.delete("all")
  select_canvas.create_text(90, 10, font=("sans-serif", 10), text="あなたの入力した数字")
  result_canvas.create_text(90, 10, font=("sans-serif", 10), text="当選番号")
  one_canvas.create_text(90, 10, font=("sans-serif", 10), text="1等賞")
  two_canvas.create_text(90, 10, font=("sans-serif", 10), text="2等賞")
  three_canvas.create_text(90, 10, font=("sans-serif", 10), text="3等賞")
  print("リセット完了")

#設定関数
def num_win_check(num):
  global num_win
  num_win = num
  return num_win


your_selects = []
candidate_numbers = []
with open("./text_file/select_number.txt", mode="w", encoding="utf-8") as fw:
  fw.write("あなたの抽選番号\n")
with open("./text_file/lottery_number.txt", mode="w", encoding="utf-8") as fw:
  fw.write("抽選番号\n")
with open("./text_file/win_one.txt", mode="w", encoding="utf-8") as fw:
  fw.write("1等賞\n")
with open("./text_file/win_two.txt", mode="w", encoding="utf-8") as fw:
  fw.write("2等賞\n")
with open("./text_file/win_three.txt", mode="w", encoding="utf-8") as fw:
  fw.write("3等賞\n")
select_flg = True
lottery_check_flg = True
candidateA_flg = True
candidateB_flg = True
develop_flg = False
n = 15
m = 15
num_win = 5
root = tkinter.Tk()
root.title("宝くじ")
root.geometry("600x450")

notebook = ttk.Notebook(root)
tab_home = tkinter.Frame(notebook)
tab_details = tkinter.Frame(notebook)
tab_setting = tkinter.Frame(notebook)
notebook.add(tab_home, text="ホーム")
notebook.add(tab_details, text="詳細情報")
notebook.add(tab_setting, text="設定")

#ホームタブ
char_lim = tab_home.register(limit_char)
entry = tkinter.Entry(tab_home, width = 6, font=("sans-serif", 30), validate="key", validatecommand=(char_lim, "%P"))
entry.place(x=35, y=100)

button_add = tkinter.Button(tab_home, height = 3, width = 15, text="追加", command=numcheck_btn)
#button.bind("<Return>", lambda event: click_btn)
button_add.place(x=40, y=160)

button_lot = tkinter.Button(tab_home, height = 3, width = 15, text="抽選", command=lottery_btn)
button_lot.place(x=40, y=220)

button_ch = tkinter.Button(tab_home, height = 3, width = 15, text="当選確認", command=lottery_check_btn)
button_ch.place(x=40, y=280)

button_reset = tkinter.Button(tab_home, height = 3, width = 15, text="リセット", command=reset_btn)
button_reset.place(x=40, y=340)

lottey_label = tkinter.Label(tab_home, font=("sans-serif", 30), text= "")

notebook.pack(expand=True, fill='both', padx=10, pady=10)

select_canvas = tkinter.Canvas(tab_home, bg="white")
select_canvas.place(x=190, y=10, width=190, height=390)

bar_y = tkinter.Scrollbar(select_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=select_canvas.yview)
select_canvas.config(yscrollcommand=bar_y.set)
select_canvas.config(scrollregion=(0, 0, 0, 2000))

select_canvas.create_text(90, 10, font=("sans-serif", 10), text="あなたの入力した数字")

result_canvas = tkinter.Canvas(tab_home, bg="white")
result_canvas.place(x=380, y=10, width=190, height=390)

bar_y = tkinter.Scrollbar(result_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=result_canvas.yview)
result_canvas.config(yscrollcommand=bar_y.set)
result_canvas.config(scrollregion=(0, 0, 0, 2000))

result_canvas.create_text(90, 10, font=("sans-serif", 10), text="当選番号")

#抽選詳細
one_canvas = tkinter.Canvas(tab_details, bg="white")
one_canvas.place(x=0, y=10, width=190, height=180)

bar_y = tkinter.Scrollbar(one_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=one_canvas.yview)
one_canvas.config(yscrollcommand=bar_y.set)
one_canvas.config(scrollregion=(0, 0, 0, 2000))

one_canvas.create_text(90, 10, font=("sans-serif", 10), text="1等賞")

two_canvas = tkinter.Canvas(tab_details, bg="white")
two_canvas.place(x=190, y=10, width=190, height=180)

bar_y = tkinter.Scrollbar(two_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=two_canvas.yview)
two_canvas.config(yscrollcommand=bar_y.set)
two_canvas.config(scrollregion=(0, 0, 0, 2000))

two_canvas.create_text(90, 10, font=("sans-serif", 10), text="2等賞")

three_canvas = tkinter.Canvas(tab_details, bg="white")
three_canvas.place(x=380, y=10, width=190, height=180)

bar_y = tkinter.Scrollbar(three_canvas, orient=tkinter.VERTICAL)
bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
bar_y.config(command=three_canvas.yview)
three_canvas.config(yscrollcommand=bar_y.set)
three_canvas.config(scrollregion=(0, 0, 0, 2000))

three_canvas.create_text(90, 10, font=("sans-serif", 10), text="3等賞")

#設定タブ
num_win_label = tkinter.Label(tab_setting, font=("sans-serif", 15), text= "当選番号数", foreground="black", background="white")
num_win_label.place(x=10, y=10)

var = tkinter.IntVar(root)
var.set(num_win)
spinbox = tkinter.Spinbox(tab_setting, width=5, font=("sans-serif", 15), textvariable=var, from_=1, to=10, increment=1, command=lambda:num_win_check(var.get()))
spinbox.configure(state="readonly")
spinbox.place(x=25, y=40)

button_normal = tkinter.Button(tab_setting, height = 3, width = 15, text="ノーマルモード", command=normal_btn)
button_normal.place(x=250, y=10)

button_develop = tkinter.Button(tab_setting, height = 3, width = 15, text="開発モード", command=develop_btn)
button_develop.place(x=400, y=10)

root.mainloop()

#your_select = list(map(int,input("6桁の数字を入力してください：").split()))




