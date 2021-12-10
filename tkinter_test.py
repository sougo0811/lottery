"""
import tkinter


app = tkinter.Tk()

app.geometry('600x450')

app.title('test')

canvas = tkinter.Canvas(app, width = 600, height = 450, background = 'white')

canvas.pack()

label = tkinter.Label(app, font=("sans-serif", 30), text= "It's a test", background="white")
label.place(x = 200, y = 200)

button = tkinter.Button(app, font=("sans-serif", 30), text="click", background="lightblue")
button.place(x = 200, y = 250)

app.mainloop()
"""

"""
import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("400x300")  # 横400x縦300

    # Canvasを生成
    canvas = tk.Canvas(root, bg="white")
    canvas.place(x=0, y=0, width=200, height=300)   # 処理位置的にここが良さそう

    # Scrollbarを生成してCanvasに配置処理
    bar_y = tk.Scrollbar(canvas, orient=tk.VERTICAL)
    bar_x = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)
    bar_y.pack(side=tk.RIGHT, fill=tk.Y)
    bar_x.pack(side=tk.BOTTOM, fill=tk.X)
    bar_y.config(command=canvas.yview)
    bar_x.config(command=canvas.xview)
    canvas.config(yscrollcommand=bar_y.set, xscrollcommand=bar_x.set)
    # Canvasのスクロール範囲を設定
    canvas.config(scrollregion=(0, 0, 300, 500))
    # self.canvas.pack(anchor=tk.NW, side=tk.LEFT)

    # 確認用の矩形表示
    canvas.create_rectangle(10, 10, 100, 100, fill='green')
    root.mainloop()


if __name__ == "__main__":
    main()
"""

import tkinter as tk


def insert(event):
    entry1.configure(state='normal')
    entry1.insert('end', 'hello')
    entry1.configure(state='readonly')


root = tk.Tk()
label1 = tk.Label(root, text="利用者ID",width=10,height=2,bd=1,relief="ridge")
label1.grid(row=1,column=1,padx=10)
entry1 = tk.Entry(root,text="",width=15)
entry1.grid(row=1,column=2,ipady=5,pady=10,padx=10)
root.bind('<Escape>', insert)  # テキストを挿入する
root.mainloop()