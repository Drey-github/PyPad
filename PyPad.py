import tkinter as tk
from tkinter.filedialog import *
from os import system


root = tk.Tk()
root.title("PyPad(主)")

flag = 0

def top(extra=0):
    global flag
    global button6
    if flag == 0:
        root.attributes('-topmost', True)
        flag = 1
        button6.config(text='取消置顶')
    else:
        root.attributes('-topmost', False)
        flag = 0
        button6.config(text='置顶')


def save(extra=0):
    filenewpath = asksaveasfilename(defaultextension='.py')
    if filenewpath != "":
        f = open(filenewpath, "w")
        f.write(text.get("1.0", "end"))
        f.close()


def run(extra=0):
    print("PyPad>>>")
    exec(text.get("1.0", "end"))
    print("<<<PyPad")


def delet():
    text.delete('1.0', 'end')


def file(extra=0):
    path = askopenfilename()
    if path != "":
        f = open(path, "r")
        a = f.read()
        f.close()
        text.insert("end", a)


def new(extra=0):
    root = tk.Tk()
    root.title("PyPad(副)")

    def save(extra):
        filenewpath = asksaveasfilename(defaultextension='.py')
        if filenewpath != "":
            f = open(filenewpath, "w")
            f.write(text.get("1.0", "end"))
            f.close()

    def run(extra):
        print("PyPad>>>")
        exec(text.get("1.0", "end"))
        print("<<<PyPad")

    def delet():
        text.delete('1.0', 'end')

    def file(extra):
        path = askopenfilename()
        if path != "":
            f = open(path, "r")
            a = f.read()
            f.close()
            text.insert("end", a)

    text = tk.Text(root)
    text.config(font=('Arial', 12), wrap='word')
    text.config(height=10, width=50)
    text.bind('<Control-s>', save)
    text.bind('<F5>', save)
    text.bind('<Control-o>', file)
    text.pack(side="bottom")

    botton1 = tk.Button(root, text="保存", command=save)
    botton1.pack(side="left")

    button2 = tk.Button(root, text="运行", command=run)
    button2.pack(side="left")

    button3 = tk.Button(root, text="清空", command=delet)
    button3.pack(side="left")

    button4 = tk.Button(root, text="打开", command=file)
    button4.pack(side="left")

    root.resizable(width=False, height=False)
    root.mainloop()


text = tk.Text(root)
text.config(font=('Arial', 12), wrap='word')
text.config(height=10, width=50)
text.bind('<Control-s>', save)
text.bind('<F5>', run)
text.bind('<Control-o>', file)
text.bind('<Control-n>', new)
text.bind('<Control-t>', top)
text.pack(side="bottom")


botton1 = tk.Button(root, text="保存", command=save)
botton1.pack(side="left")

button2 = tk.Button(root, text="运行", command=run)
button2.pack(side="left")

button3 = tk.Button(root, text="清空", command=delet)
button3.pack(side="left")

button4 = tk.Button(root, text="打开", command=file)
button4.pack(side="left")

button5 = tk.Button(root, text="新建", command=new)
button5.pack(side="left")

button6 = tk.Button(root, text="置顶", command=top)
button6.pack(side="left")

root.resizable(width=False, height=False)
root.mainloop()
