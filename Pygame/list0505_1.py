import pygame
import sys

img_galaxy = pygame.image.load("Pygame\image\galaxy.png")
img_sship = pygame.image.load("Pygame\image\starship.png")

def main():
    pygame.init()
    pygame.display.set_caption("Pygame 사용법")
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    ang = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((960, 720), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((960, 720))

        screen.blit(img_galaxy, [0, 0]) #별 이미지 그리기

        ang = (ang + 1) % 360 #회전 각도 증가
        img_rz = pygame.transform.rotozoom(img_sship, ang, 1.0) #회전한 우주선 이미지 생성
        x = 480 - img_rz.get_width() / 2 #x 좌표 계산
        y = 360 - img_rz.get_height() / 2 #y 좌표 계산
        screen.blit(img_rz, [x, y]) #회전할 우주선 이미지 그리기

        pygame.display.update() #화면 업데이트
        clock.tick(30) #30프레임씩 반복

if __name__ == '__main__':
    main()
    