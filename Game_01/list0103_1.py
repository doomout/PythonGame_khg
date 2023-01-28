import tkinter

root = tkinter.Tk()
root.title("Canvas에 화면 그리기")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="Game_01\img\park.png") #vs code 에선 폴더 경로도 써줘야 한다.
canvas.create_image(240, 150, image=img_bg)
root.mainloop()
