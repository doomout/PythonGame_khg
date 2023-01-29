# 파이썬으로 게임 개발  
파이썬 버전 : 3.11.1  
사용 IDE : vs code  
사용 OS : 윈도우10, 맥 os (공부 환경에 따라 바꿔서 개발)  
참고 도서 : 파이썬으로 배우는 게임 개발 실전편   
목표 : 게임 개발을 하며 개발 스킬을 향상 시킨다.  
1. bind() 명령으로 얻을 수 있는 주요 이벤트
```py
<KeyPress>, <Key> : 키를 누름  
<KeyRelease> : 키룰 눌렀다 뗌  
<Motion> : 마우스 포인터 이동  
<ButtonPress>, <Button> : 마우스 버튼 누름  
<ButtonRelease> : 마우스 버튼 눌렀다 뗌  
```
2. format() 명령 문자열의 {}를 인수 값으로 적용
```py
d = datetime.datetime.now() #현재 시간 저장
t = "{0}:{1}:{2}".format(d.hour, d.minute, d.second) #시분초 저장
```
3. tkinter.PhotoImage()를 이용하여 이미지 읽을 때 주의점  
```py
img_bg = tkinter.PhotoImage(file="Game_01\img\park.png") #vs code 에선 폴더 경로도 써줘야 한다.
```
4. % 연산자를 이용한 인덱스 선택법
```py
#ani 가 0인 경우 계산식은 (0 + 1) % 4는 1이 대입 된다.
#ani 가 1인 경우 계산식은 (1 + 1) % 4는 2이 대입 된다.
#ani 가 2인 경우 계산식은 (2 + 1) % 4는 3이 대입 된다.
#ani 가 3인 경우 계산식은 (3 + 1) % 4는 0이 대입 된다.
ani = (ani + 1) % 4 

#image=img_dog[ani]를 통해 해당 이미지의 인덱스 값을 넣는다.
canvas.create_image(240, 200, image=img_dog[ani], tag="BG") 
```
5. 사각형 체크 함수
```py
def hit_check_rect():
    dx = abs((x1 + w1 / 2) - (x2 + w2 / 2)) #두 사각형의 x방향 거리 대입
    dy = abs((y1 + h1 / 2) - (y2 + h2 / 2)) #두 사각형의 y방향 거리 대입
    #사각형이 겹치는 조건 판정
    if dx <= w1 / 2 + w2 / 2 and dy <= h1 / 2 + h2 / 2: 
        return True
    return False
```
6. 원 체크 함수
```py
def hit_check_circle():
    #두 점 사이 거리를 계산해서 대입
    dis = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    #dis 값이 두 원의 반지름의 합 이하라면
    if dis <= r1 + r2:
        return True
    return False
```