import tkinter

root = tkinter.Tk()
root.title("맵 데이터")
canvas = tkinter.Canvas(width=336, height=240)
canvas.pack()
img = [
    tkinter.PhotoImage(file="Game_01\img\chip0.png"),
    tkinter.PhotoImage(file="Game_01\img\chip1.png"),
    tkinter.PhotoImage(file="Game_01\img\chip2.png"),
    tkinter.PhotoImage(file="Game_01\img\chip3.png")
]
map_data = [
    [0,1,0,2,2,2,2],
    [3,0,0,0,2,2,2],
    [3,0,0,1,0,0,0],
    [3,3,0,0,0,0,1],
    [3,3,3,3,0,0,0]
]

for y in range(5):
    for x in range(7):
        n = map_data[y][x]
        canvas.create_image(x*48+24, y*48+24, image=img[n]) #맵칩의 사이즈가 가로, 세로 48픽셀이기에 *48을 한다.

root.mainloop()