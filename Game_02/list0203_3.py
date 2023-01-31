import tkinter
import math

root = tkinter.Tk()
root.title("삼각함수를 활용한 선 그리기")
canvas = tkinter.Canvas(width=400,height=400, bg="white")
canvas.pack() #캔버스 배치
#d 값이 0~90까지 10씩 증가
for d in range(0, 90, 10):
    a = math.radians(d) #d값을 라디안으로 변환해서 a에 대입
    x = 300 * math.cos(a) #선 끝의 x좌표를 cos으로 계산
    y = 300 * math.sin(a) #선 끝의 y좌표를 sin으로 계산
    #(0,0)에서 (x,y)까지 선 그음
    canvas.create_line(0,0,x,y, fill="blue") 

root.mainloop()
