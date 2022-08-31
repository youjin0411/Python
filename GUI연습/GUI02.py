from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")
e=Entry(root, width = 30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END)) # 1: 첫번째 라인, 0: 0번째 column위치
    print(e.get()) #엔트리에 있던거
    
    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
    
    # 입력을 받거나 보여주기 위해 -차이
    # >텍스트: 여러줄 입력받음
    # >엔트리: 한줄만 입력받음
    
btn = Button(root, text="클릭", command = btncmd)
btn.pack


root.mainloop()