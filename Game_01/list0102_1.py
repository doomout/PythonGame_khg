import tkinter
import datetime

def time_now():
    d = datetime.datetime.now() #현재 시간 저장
    t = "{0}:{1}:{2}".format(d.hour, d.minute, d.second) #시분초 저장
    label["text"] = t #문자열로 반환
    root.after(1000, time_now) #1초 후 다시 함수 실행

root = tkinter.Tk()
root.geometry("400x100")
root.title("간이 계산")
label = tkinter.Label(font=("Times New Roman", 60))
label.pack()
time_now()
root.mainloop()