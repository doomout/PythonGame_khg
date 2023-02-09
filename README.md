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
7. 버튼에 함수 연결법, 예외 처리법
```py
def trigo(): 
    try: #예외가 발생할 가능성이 있는 코드
        d=float(entry.get())
        a=math.radians(d) #라디안 값으로 변환
        s=math.sin(a)
        c=math.cos(a)
        t=math.tan(a)
        label_s["text"] = "sin " + str(s)
        label_c["text"] = "cos " + str(c)
        label_t["text"] = "tan " + str(t)
    except: #예외가 발생했을 때 실행
        print("각도를 도 값으로 입력해 주세요.")

#버튼 생성, 버튼 클릭시 실행 함수 지정
button = tkinter.Button(text="계산",command=trigo) 
```
8. Pygame 설치시 주의점  
 -현재 pygame는 python 3.11 버전을 지원하지 않기에 pre-release 버전을 설치해야 한다.  
 -명령어 : pip3 install pygame --pre   
   
9. Pygame 키 이벤트 함수(화면 크기 전환)
```py
 while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1: #F1키
                screen = pygame.display.set_mode((960, 720), pygame.FULLSCREEN) #전체 화면
            if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE: #F2키나 ESC 키
                screen = pygame.display.set_mode((960, 720)) #일반 사이즈로 전환

    screen.blit(img_galaxy, [0, 0]) #이미지 그리기
    pygame.display.update() #화면 업데이트
    clock.tick(30) #30프레임 마다 반복
```
10. 이미지 회전 함수
```py
while True:
    screen.blit(img_galaxy, [0, 0]) #별 이미지(배경) 그리기

    ang = (ang + 1) % 360 #회전 각도 증가
    img_rz = pygame.transform.rotozoom(img_sship, ang, 1.0) #회전한 우주선 이미지 생성
    x = 480 - img_rz.get_width() / 2 #x 좌표 계산
    y = 360 - img_rz.get_height() / 2 #y 좌표 계산
    screen.blit(img_rz, [x, y]) #회전할 우주선 이미지 그리기

    pygame.display.update() #화면 업데이트
    clock.tick(30) #30프레임씩 반복
```