import tkinter

def key_down(e):
    key_c = e.keycode
    label1["text"] = "keyCode: " + str(key_c)
    key_s = e.keysym
    label2["text"] = "keyName: " + key_s

root = tkinter.Tk()
root.geometry("400x200")
root.title("키 입력")
root.bind("<KeyPress>", key_down) #키를 눌렀을 때 사용할 함수 지정
fnt = ("Times New Roman", 30) #폰트 정의
label1 = tkinter.Label(text="keyCode: ", font=fnt)
label1.place(x=0,y=0)
label2 = tkinter.Label(text="keyName: ", font=fnt)
label2.place(x=0,y=80)
root.mainloop()