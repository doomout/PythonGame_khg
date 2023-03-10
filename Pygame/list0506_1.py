import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (192, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init() #모듈 초기화
    pygame.display.set_caption("Pygame 사용법")
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)

    while True:
        for event in pygame.event.get(): #이벤트 반복처리
            if event.type == pygame.QUIT: #x버튼 누르면...
                pygame.quit() #pygame 모듈 초기화
                sys.exit() #프로그램 종료

        screen.fill(BLACK) #지정한 색상으로 화면 전체를 채움

        key = pygame.key.get_pressed() #리스트 key에 모든 키 상태 입력
        txt1 = font.render("UP{}  DOWN{}".format(key[pygame.K_UP], key[pygame.K_DOWN]), True, WHITE, GREEN)
        txt2 = font.render("LEFT{}  RIGHT{}".format(key[pygame.K_LEFT], key[pygame.K_RIGHT]), True, WHITE, BLUE)
        txt3 = font.render("SPACE{}  Z{}".format(key[pygame.K_SPACE], key[pygame.K_z]), True, WHITE, BROWN)
        screen.blit(txt1, [200, 100])
        screen.blit(txt2, [200, 300])
        screen.blit(txt3, [200, 500])

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
