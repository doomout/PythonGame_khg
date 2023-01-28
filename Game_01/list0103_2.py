import tkinter

x = 0
def scroll_bg():
    global x
    x = x + 1 
    if x == 480: # x가 480이 되면
        x = 0 # x에 0 대입
    canvas.delete("BG") #먼저 배경 이미지 삭제
    canvas.create_image(x - 240, 150, image=img_bg, tag="BG") #배경 이미지 그리기(왼쪽)
    canvas.create_image(x + 240, 150, image=img_bg, tag="BG") #배경 이미지 그리기(오른쪽)
    root.after(50, scroll_bg) #50밀리 초 후 함수 재실행

root = tkinter.Tk()
root.title("화면 스크롤")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="Game_01\img\park.png")
scroll_bg()
root.mainloop()
