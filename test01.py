from tkinter import *

window = Tk()
program = Label(window, text="간단한 GUI 프로그램 ! ")
program.pack()

firstBtn = Button(window, text="환영합니다.")
lastBtn = Button(window, text="종료")

firstBtn.pack()
lastBtn.pack()

window.mainloop()