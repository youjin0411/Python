from itertools import count
import tkinter
win = tkinter.Tk()

#버튼 만들기 + 옵션 설정
btn = tkinter.Button(win, text='btn', background='yellow')

#버튼 옵션 설정 
btn.config(width=5, height= 2)
btn.config(text="button")

#버튼 배치하기 
btn.pack()

win.mainloop()

import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

app = tk.Tk()
buttonExample = tk.Button(app, 
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()