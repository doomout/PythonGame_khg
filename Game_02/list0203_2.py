import math
import tkinter


def trigo():
    try: #예외처리
        d=float(entry.get())
        a=math.radians(d) #라디안 값으로 변환
        s=math.sin(a)
        c=math.cos(a)
        t=math.tan(a)
        label_s["text"] = "sin " + str(s)
        label_c["text"] = "cos " + str(c)
        label_t["text"] = "tan " + str(t)
    except:
        print("각도를 도 값으로 입력해 주세요.")

root = tkinter.Tk() #윈도우 객체 생성
root.geometry("300x200") #윈도우 크기 지정
root.title("삼각 함수 값") #윈도우 타이틀 지정

entry = tkinter.Entry(width=10) #텍스트 입력 필드 지정
entry.place(x=20,y=20) #텍스트 입력 위치 지정

button = tkinter.Button(text="계산",command=trigo) #버튼 생성, 버튼 클릭시 실행 함수 지정
button.place(x=100,y=20) #버튼 위치 지정

label_s=tkinter.Label(text="sin")
label_s.place(x=20, y=60)

label_c=tkinter.Label(text="con")
label_c.place(x=20, y=100)

label_t=tkinter.Label(text="tan")
label_t.place(x=20, y=140)

root.mainloop()