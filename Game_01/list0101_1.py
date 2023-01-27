import tkinter

root = tkinter.Tk() #윈도우 객체 생성
root.geometry("400x200") #윈도우 크기 지정
root.title("파이썬에서 GUI 다루기") #윈도우 타이틀 지정
label=tkinter.Label(root, text="게임 개발 첫걸음", font=("Time New Roman", 20)) #라벨 컴포넌트 생성
label.place(x=80, y=60)#라벨 배치
root.mainloop() #윈도우 표시