import pygame
import sys

WHITE = (255, 255, 255) #색 정의 : 흰색
BLACK = (0, 0, 0) #색 정의 : 검정

def main():
    pygame.init() #모듈 초기화
    pygame.display.set_caption("Pygame 사용법")  #타이틀
    screen = pygame.display.set_mode((800, 600)) #창 사이즈
    clock = pygame.time.Clock() #clock() 초기화
    font = pygame.font.Font(None, 80) #폰트 초기화
    tmr = 0 #시간 변수

    while True:
        for event in pygame.event.get(): #이벤트 반복
            if event.type == pygame.QUIT: #x 버튼 누른다면...
                pygame.quit() #pygame 초기화 해제
                sys.exit() #프로그램 종료

        screen.fill(BLACK) #화면 전체 검정으로 설정

        tmr = tmr + 1
        col = (0, tmr % 256, 0) #색 지정
        pygame.draw.rect(screen, col, [100, 100, 600, 400]) #사각형 그림
        sur = font.render(str(tmr), True, WHITE) #흰색 문자열 표시
        screen.blit(sur, [300, 200]) #문자열을 스크린에 표시

        pygame.display.update() #화면 업데이트
        clock.tick(30)

if __name__ == '__main__':
    main()
