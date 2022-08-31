from tkinter import *

root = Tk()
root.title("Nado GUI")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="img/img.jpg")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    global photo2 #전역변수로 해서 갈비지콜렉터 피해 
    photo2 = PhotoImage(file="img/img2.jpg")
    label2.config(text=photo2   )
    
btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()