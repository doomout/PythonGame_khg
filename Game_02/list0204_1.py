#index 값
#0 = 타이틀 화면
#1 = 게임 플레이 중 상태
#2 = 게임 오버 화면

import tkinter

fnt1 = ("Times New Roman", 20) #폰트 정의(작은크기)
fnt2 = ("Times New Roman", 40) #폰트 정의(큰 크기)
index = 0 #인덱스 변수
timer = 0 #타이머 변수

key = "" #키 값을 대입할 변수
def key_down(e):
    global key
    key = e.keysym
    
def main():
    global index, timer #전역 변수 선언
    canvas.delete("STATUS") 
    timer = timer + 1
    canvas.create_text(200, 30, text="index " + str(index), fill="white", font=fnt1, tag="STATUS") #index 값 표시
    canvas.create_text(400, 30, text="timer " + str(index), fill="cyan", font=fnt1, tag="STATUS") #timer 값 표시
    if index == 0: #index 0처리(타이틀 화면)
        if timer == 1: #timer 값이 1이면
            canvas.create_text(300, 150, text="타이틀", fill="white", font=fnt2, tag="TITLE") #타이틀 문자 표시
            canvas.create_text(300, 300, text="Press[SPACE]key", fill="lime", font=fnt1, tag="TITLE") #Press[SPACE]key 문자열 표시
        if key == "space": #스페이스를 눌렀다면
            canvas.delete("TITLE") #타이틀 문자 삭제
            canvas.create_rectangle(0,0,600,400,fill="blue",tag="GAME")#캔버스를 파란색으로 칠함
            canvas.create_text(300,150,text="게임 중",fill="white",font=fnt2, tag="GAME") #게임중 문자열 표시
            canvas.create_text(300,300,text="[E]종료",fill="yellow", font=fnt1, tag="GAME") #E 종료 문자열 표시
            index = 1 #인덱스 값을 1로 변경
            timer = 0 #timer 값을 0으로 변경
            
    if index == 1: #index 1처리(플레이 중 화면)
        if key == "e": #e를 눌렀다면
            canvas.delete("GAME")
            canvas.create_rectangle(0,0,600,400, fill="maroon", tag="OVER")
            canvas.create_text(300,150,text="GAME OVER", fill="red",font=fnt2, tag="OVER")
            index = 2
            timer = 0
            
    if index == 2:
        if timer == 30: 
            canvas.delete("OVER")
            index = 0
            timer = 0
            
    root.after(100, main)
                 
root = tkinter.Tk()
root.title("인덱스와 타이머")
root.bind("<KeyPress>", key_down)
canvas = tkinter.Canvas(width=600, height=400, bg="black")
canvas.pack()
main()
root.mainloop()