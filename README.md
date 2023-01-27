# 파이썬으로 게임 개발  
파이썬 버전 : 3.10.1  
사용 IDE : vs code  
사용 OS : 윈도우10, 맥 os (공부 환경에 따라 바꿔서 개발)  
참고 도서 : 파이썬으로 배우는 게임 개발 실전편   
목표 : 게임 개발을 하며 개발 스킬을 향상 시킨다.  
1. bind() 명령으로 얻을 수 있는 주요 이벤트
<KeyPress>, <Key> : 키를 누름  
<KeyRelease> : 키룰 눌렀다 뗌  
<Motion> : 마우스 포인터 이동  
<ButtonPress>, <Button> : 마우스 버튼 누름  
<ButtonRelease> : 마우스 버튼 눌렀다 뗌  
2. format() 명령 문자열의 {}를 인수 값으로 적용
```py
d = datetime.datetime.now() #현재 시간 저장
t = "{0}:{1}:{2}".format(d.hour, d.minute, d.second) #시분초 저장
```
