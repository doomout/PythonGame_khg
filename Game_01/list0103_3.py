import tkinter

x=0
ani = 0
def animation():
    global x, ani
    x = x + 4
    if x == 480:
        x = 0
    canvas.delete("BG") #먼저 배경 이미지 삭제
    canvas.create_image(x - 240, 150, image=img_bg, tag="BG") #배경 이미지 그리기(왼쪽)
    canvas.create_image(x + 240, 150, image=img_bg, tag="BG") #배경 이미지 그리기(오른쪽)
    ani = (ani + 1) % 4 # ani 값을 0~3 범위에서 변경
    canvas.create_image(240, 200, image=img_dog[ani], tag="BG") #개 이미지 그림
    root.after(200, animation) #200밀리 초 후 함수 재실행

root = tkinter.Tk()
root.title("애니메이션")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="Game_01\park.png") #배경 이미지 1장
img_dog = [ #개 이미지 4장
    tkinter.PhotoImage(file="Game_01\dog0.png"),
    tkinter.PhotoImage(file="Game_01\dog1.png"),
    tkinter.PhotoImage(file="Game_01\dog2.png"),
    tkinter.PhotoImage(file="Game_01\dog3.png")
]
animation()
root.mainloop()