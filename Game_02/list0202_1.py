import tkinter
import math

def hit_check_circle():
    #두 점 사이 거리를 계산해서 대입
    dis = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    #dis 값이 두 원의 반지름의 합 이하라면
    if dis <= r1 + r2:
        return True
    return False

def mouse_move(e):
    #전역 변수 선언
    global x1, y1
    x1 = e.x #초록색 원의 x좌표를 포인터 좌표로 함
    y1 = e.y #초록색 원의 y좌표를 포인터 좌표로 함
    col = "green"
    #두 원이 접촉 했다면
    if hit_check_circle() == True:
        col = "lime" #lime 문자열로 변경
    canvas.delete("CIR1") #기존 초록색 원 삭제
    canvas.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill=col, tag="CIR1") #원 그리기
    
root = tkinter.Tk()
root.title("원을 사용한 히트 체크")
canvas = tkinter.Canvas(width=600, height=400, bg="white")
canvas.pack()
canvas.bind("<Motion>", mouse_move)

x1=50 #초록색 원 중심 x좌표
y1=50 #초록색 원 중심 y좌표
r1=40 #초록색 원 반지름

canvas.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill="green", tag="CIR1") #초록색 원 그림

x2=300 #주황색 원 중심 x좌표
y2=200 #주황색 원 중심 y좌표
r2=80 #주황색 원 반지름
canvas.create_oval(x2-r2, y2-r2, x2+r2, y2+r2, fill="orange") #주황색 원 그림

root.mainloop()