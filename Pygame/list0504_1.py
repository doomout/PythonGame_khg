import pygame
import sys

img_galaxy = pygame.image.load("Pygame/image/galaxy.png") #배경 별 이미지

def main():
    pygame.init()#chrlghk
    pygame.display.set_caption("Pygame 사용법")
    screen = pygame.display.set_mode((960, 720)) #창 사이즈
    clock = pygame.time.Clock()

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

if __name__ == '__main__':
    main()
