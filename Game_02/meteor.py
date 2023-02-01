import tkinter
import random

fnt1 = ("Times New Roman", 24)
fnt2 = ("Times New Roman", 50)
index = 0 #게임 진행 관리
timer = 0 #게임 진행 관리
score = 0 #점수
bg_pos=0 #배경 스크롤을 위한 좌표
px = 240 #우주선 좌표
py = 540 #우주선 좌표
METEO_MAX = 30 #화면에 흐르는 유성 수
mx = [0] * METEO_MAX #유성 좌표
my = [0] * METEO_MAX #유성 좌표

key = ""
koff = False
def key_down(e): #키 눌렀을 때 실행
    global key, koff
    key = e.keysym
    koff = False
    
def key_up(e): # 키를 눌렀다 땠을 때 실행
    global koff
    koff = True
   
def main(): #메인 처리 실행
    global key, koff, index, timer, score, bg_pos, px
    timer = timer + 1
    bg_pos = (bg_pos + 1) % 640
    canvas.delete("SCREEN")
    canvas.create_image(240, bg_pos - 320, image=img_bg, tag="SCREEN")
    canvas.create_image(240, bg_pos + 320, image=img_bg, tag="SCREEN")
     #0: 타이틀 화면 - 스페이스 키를 누르면 각 변수를 초기화 하고 1로 이동
    if index == 0:
        canvas.create_text(240, 240, text="METEOR", fill="gold",font=fnt2, tag="SCREEN")
        canvas.create_text(240, 480, text="Press [SPACE] Key", fill="lime",font=fnt1, tag="SCREEN")
        if key == "space":
            score = 0
            px = 240
            init_enemy()
            index = 1
    #1: 게임 플레이 화면
    if index == 1:
        score = score + 1
        move_player() #우주선 이동
        move_enemy() #유성 이동
    #게임 오버 화면
    if index == 2:
        move_enemy()
        canvas.create_text(240,timer * 4, text="GAME OVER", fill="red", font=fnt2, tag="SCREEN")
        if timer == 60:
            index = 0
            timer = 0
    canvas.create_text(240, 30, text="SCORE " + str(score), fill="white", font=fnt1, tag="SCREEN")
    if koff == True:
        key = ""
        koff = False
    root.after(50, main)
        
def hit_check(x1, y1, x2, y2): #두 점 사이 거리로 히트 체크 수행
    if((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2) < 36 * 36):
        return True
    return False

def init_enemy(): #유성 좌표 초기화
    for i in range(METEO_MAX):
        mx[i] = random.randint(0, 480)
        my[i] = random.randint(-640, 0)
    
def move_enemy(): #유성 이동
    global index, timer
    for i in range(METEO_MAX):
        my[i] = my[i] + 6 + i /5
        if my[i] > 660:
            mx[i] = random.randrange(0,480)
            my[i] = random.randrange(-640, 0)
        if index == 1 and hit_check(px,py,mx[i], my[i]) == True:
            index = 2
            timer = 0
        canvas.create_image(mx[i],my[i], image=img_enemy, tag="SCREEN")
    
def move_player(): #우주선 이동
    global px
    if key == "Left" and px>30:
        px = px - 10
    if key == "Right" and px < 450:
        px = px + 10
    canvas.create_image(px, py, image=img_player[timer % 2], tag="SCREEN")
    
root = tkinter.Tk()
root.title("Mini Game")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=480, height=640)
canvas.pack()
img_player = [
    tkinter.PhotoImage(file="Game_02\img\starship0.png"),
    tkinter.PhotoImage(file="Game_02\img\starship1.png")
]
img_enemy = tkinter.PhotoImage(file="Game_02\img\meteo.png")
img_bg = tkinter.PhotoImage(file="Game_02\img\cosmo.png")
main()
root.mainloop()